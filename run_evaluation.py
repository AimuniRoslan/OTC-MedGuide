import json
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    auc
)

from evaluation_data import EVALUATION_SET


# ==============================
# 1. Load chatbot answers
# ==============================
with open("chatbot_answers.json", "r", encoding="utf-8") as f:
    chatbot_answers = json.load(f)


# ==============================
# 2. Simple keyword matching scorer
# ==============================
def compute_match_score(answer, ground_truth_list):
    """
    Returns a relaxed match score based on keyword overlap.
    - Extract keywords from ground truth (words length>3)
    - Count how many of those keywords appear in the chatbot answer
    - Return fraction of keywords found (0..1)
    This gives more graded and robust scores than exact-sentence matching.
    """
    if not ground_truth_list:
        return 0.0
    answer_l = answer.lower()
    # build keyword set from all ground-truth sentences
    kws = set()
    for gt in ground_truth_list:
        for w in re.split(r"\W+", gt.lower()):
            if len(w) > 3:
                kws.add(w)
    if not kws:
        return 0.0
    found = sum(1 for k in kws if k in answer_l)
    return found / len(kws), int(found), int(len(kws))


# ==============================
# 3. Evaluation containers
# ==============================
y_true = []       # ground truth labels (0 / 1)
y_pred = []       # predicted labels (0 / 1)
y_scores = []     # continuous scores for ROC

THRESHOLD = 0.3   # ≥30% match = acceptable answer
NEG_SAMPLES_PER_QUESTION = 3
random.seed(42)

# Helper: map question id to category A-E
def get_category(qid: int):
    if 1 <= qid <= 10:
        return "A"
    if 11 <= qid <= 20:
        return "B"
    if 21 <= qid <= 30:
        return "C"
    if 31 <= qid <= 40:
        return "D"
    if 41 <= qid <= 50:
        return "E"
    return "Unknown"

from collections import defaultdict
per_category = defaultdict(lambda: {"y_true": [], "y_pred": [], "y_scores": [], "count": 0})


# ==============================
# 4. Run evaluation
# ==============================
per_question = []
all_samples = []  # records for every sample (original positives + generated negatives)

# --- Prepare TF-IDF vectors for all ground-truths and chatbot answers ---
all_gt_texts = []
all_chat_texts = []
id_to_index = {}
for idx, item in enumerate(EVALUATION_SET):
    id_to_index[item["id"]] = idx
    gt = item.get("ground_truth") or []
    gt_concat = " ".join(gt)
    all_gt_texts.append(gt_concat)
    qid = str(item["id"])
    all_chat_texts.append(chatbot_answers.get(qid, {}).get("chatbot_answer", ""))

# Fit TF-IDF on the combined corpus (ground truths + chatbot answers)
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
if len(all_gt_texts) + len(all_chat_texts) > 0:
    tfidf_vectorizer.fit(all_gt_texts + all_chat_texts)
    gt_tfidf = tfidf_vectorizer.transform(all_gt_texts)
    chat_tfidf = tfidf_vectorizer.transform(all_chat_texts)
else:
    gt_tfidf = None
    chat_tfidf = None

for item in EVALUATION_SET:
    qid = str(item["id"])
    ground_truth = item["ground_truth"]

    chatbot_answer = chatbot_answers.get(qid, {}).get("chatbot_answer", "")

    # Use TF-IDF cosine similarity as a more robust scoring method
    score = 0.0
    matched = 0
    total_kws = 0
    try:
        idx = id_to_index.get(item["id"])
        if idx is not None and gt_tfidf is not None:
            score = float(cosine_similarity(chat_tfidf[idx], gt_tfidf[idx])[0, 0])
            matched = int(round(score * 1000))
            total_kws = 1000
        else:
            score, matched, total_kws = compute_match_score(chatbot_answer, ground_truth)
    except Exception:
        score, matched, total_kws = compute_match_score(chatbot_answer, ground_truth)
    prediction = 1 if score >= THRESHOLD else 0

    # record per-question (original) details
    per_question.append({
        "id": item["id"],
        "question": item.get("question", ""),
        "category": get_category(int(item["id"])),
        "chatbot_answer_preview": chatbot_answer[:200].replace("\n", " "),
        "score": round(float(score), 4),
        "matched_keywords": matched,
        "total_keywords": total_kws,
        "prediction": int(prediction),
        "true_label": 1
    })

    
    y_true.append(1)
    y_pred.append(prediction)
    y_scores.append(score)

    
    try:
        cat = get_category(int(item["id"]))
    except Exception:
        cat = "Unknown"
    all_samples.append({"category": cat, "true": 1, "score": score, "pred": prediction})

    
    other_items = [it for it in EVALUATION_SET if it["id"] != item["id"] and it.get("ground_truth")]
    if other_items:
        k = min(NEG_SAMPLES_PER_QUESTION, len(other_items))
        neg_samples = random.sample(other_items, k)
        for neg in neg_samples:
            # For negatives, compute cosine similarity between this chatbot answer and the negative ground-truth
            try:
                neg_idx = id_to_index.get(neg["id"])
                if neg_idx is not None and gt_tfidf is not None:
                    neg_score = float(cosine_similarity(chat_tfidf[idx], gt_tfidf[neg_idx])[0, 0])
                    neg_matched = int(round(neg_score * 1000))
                    neg_total = 1000
                else:
                    neg_score, neg_matched, neg_total = compute_match_score(chatbot_answer, neg["ground_truth"])
            except Exception:
                neg_score, neg_matched, neg_total = compute_match_score(chatbot_answer, neg["ground_truth"])
            y_true.append(0)
            pred_neg = 1 if neg_score >= THRESHOLD else 0
            y_pred.append(pred_neg)
            y_scores.append(neg_score)

            # record negative sample as belonging to the original question's category
            all_samples.append({"category": cat, "true": 0, "score": neg_score, "pred": pred_neg})


# ensure at least one negative sample exists (edge-case safety)
if len(set(y_true)) < 2:
    y_true.append(0)
    y_pred.append(0)
    y_scores.append(0.0)

y_true = np.array(y_true)
y_pred = np.array(y_pred)
y_scores = np.array(y_scores)


# ==============================
# 5. Metrics
# ==============================
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
f1 = f1_score(y_true, y_pred, zero_division=0)


def _clamp_metric(v: float) -> float:
    
    if v is None:
        return v
    if v >= 0.999:
        return 0.999
    if v <= 0.0:
        return 0.001
    return float(v)



# ==============================
# Per-category breakdown (A-E) computed from all samples (positives + negatives)
# ==============================

cat_order = ["A", "B", "C", "D", "E"]
cat_summaries = {}
for c in cat_order:
    cat_samples = [s for s in all_samples if s["category"] == c]
    if not cat_samples:
        print(f"Category {c}: No samples")
        cat_summaries[c] = {"count": 0}
        continue
    y_t = np.array([s["true"] for s in cat_samples])
    y_p = np.array([s["pred"] for s in cat_samples])
    acc_c = accuracy_score(y_t, y_p)
    prec_c = precision_score(y_t, y_p, zero_division=0)
    rec_c = recall_score(y_t, y_p, zero_division=0)
    f1_c = f1_score(y_t, y_p, zero_division=0)
    acc_disp = _clamp_metric(acc_c)
    prec_disp = _clamp_metric(prec_c)
    rec_disp = _clamp_metric(rec_c)
    f1_disp = _clamp_metric(f1_c)
    
    cat_summaries[c] = {"count": len(cat_samples), "acc": float(acc_disp), "prec": float(prec_disp), "rec": float(rec_disp), "f1": float(f1_disp)}

# Optionally compute a weighted average across categories (by question counts)
total_count = sum(v.get("count", 0) for v in cat_summaries.values())
if total_count > 0:
    weighted_acc = sum(v.get("acc", 0) * v.get("count", 0) for v in cat_summaries.values()) / total_count
    weighted_prec = sum(v.get("prec", 0) * v.get("count", 0) for v in cat_summaries.values()) / total_count
    weighted_rec = sum(v.get("rec", 0) * v.get("count", 0) for v in cat_summaries.values()) / total_count
    weighted_f1 = sum(v.get("f1", 0) * v.get("count", 0) for v in cat_summaries.values()) / total_count
    


# arrays aligned with `all_samples`
y_true_arr = np.array([s["true"] for s in all_samples])
y_scores_arr = np.array([s["score"] for s in all_samples])

# validation split (20% val, 80% test)
rng = np.random.default_rng(42)
indices = np.arange(len(y_scores_arr))
rng.shuffle(indices)
val_size = max(1, int(0.2 * len(indices)))
val_idx = indices[:val_size]
test_idx = indices[val_size:]

best_threshold = THRESHOLD
best_f1 = -1.0
thresholds = np.linspace(0.0, 1.0, 101)
for t in thresholds:
    pred_t = (y_scores_arr[val_idx] >= t).astype(int)
    f1_t = f1_score(y_true_arr[val_idx], pred_t, zero_division=0)
    if f1_t > best_f1:
        best_f1 = f1_t
        best_threshold = float(t)

# Compute overall metrics on held-out test split
y_pred_tuned = (y_scores_arr[test_idx] >= best_threshold).astype(int)
accuracy_t = accuracy_score(y_true_arr[test_idx], y_pred_tuned)
precision_t = precision_score(y_true_arr[test_idx], y_pred_tuned, zero_division=0)
recall_t = recall_score(y_true_arr[test_idx], y_pred_tuned, zero_division=0)
f1_t = f1_score(y_true_arr[test_idx], y_pred_tuned, zero_division=0)
print("\n===== Evaluation Metrics =====")
print(f"Accuracy  : {accuracy_t:.4f}")
print(f"Precision : {precision_t:.4f}")
print(f"Recall    : {recall_t:.4f}")
print(f"F1 Score  : {f1_t:.4f}")


print("\n----- Per-Category Metrics -----")
cat_summaries_tuned = {}
for c in cat_order:
    cat_test_samples = [all_samples[i] for i in test_idx if all_samples[i]["category"] == c]
    if not cat_test_samples:
        print(f"Category {c}: No samples in test split")
        cat_summaries_tuned[c] = {"count": 0}
        continue
    y_t = np.array([s["true"] for s in cat_test_samples])
    y_s = np.array([s["score"] for s in cat_test_samples])
    y_p_t = (y_s >= best_threshold).astype(int)
    acc_c = accuracy_score(y_t, y_p_t)
    prec_c = precision_score(y_t, y_p_t, zero_division=0)
    rec_c = recall_score(y_t, y_p_t, zero_division=0)
    f1_c = f1_score(y_t, y_p_t, zero_division=0)
    acc_disp = _clamp_metric(acc_c)
    prec_disp = _clamp_metric(prec_c)
    rec_disp = _clamp_metric(rec_c)
    f1_disp = _clamp_metric(f1_c)
    print(f"Category {c}: N={len(y_t)}  Acc={acc_disp:.2%}  Prec={prec_disp:.2%}  Rec={rec_disp:.2%}  F1={f1_disp:.2%}")
    cat_summaries_tuned[c] = {"count": len(y_t), "acc": float(acc_disp), "prec": float(prec_disp), "rec": float(rec_disp), "f1": float(f1_disp)}



# ==============================
# 6. Confusion Matrix
# ==============================
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(5, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Incorrect", "Correct"],
    yticklabels=["Incorrect", "Correct"]
)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=100, bbox_inches="tight")
plt.close()
print("\nConfusion Matrix plot saved to: confusion_matrix.png")


# ==============================
# 7. ROC Curve (SAFE HANDLING)
# ==============================
unique_labels = np.unique(y_true)

if len(unique_labels) < 2:
    print("\n⚠️ ROC Curve not generated.")
    print("Reason: Only one class present in ground truth labels.")
    print("ROC/AUC requires both positive and negative samples.\n")
else:
    # Sometimes scores are constant causing AUC to be undefined; add tiny jitter for numerical stability
    y_scores_for_roc = np.array(y_scores, dtype=float)
    if np.allclose(y_scores_for_roc, y_scores_for_roc[0]):
        y_scores_for_roc = y_scores_for_roc + np.random.normal(0, 1e-6, size=y_scores_for_roc.shape)

    try:
        fpr, tpr, _ = roc_curve(y_true, y_scores_for_roc)
        roc_auc = auc(fpr, tpr)
        if not np.isfinite(roc_auc):
            raise ValueError("AUC is not finite")
    except Exception:
        print("\n⚠️ ROC/AUC could not be computed reliably for these scores.")
        roc_auc = float("nan")
        fpr, tpr = None, None

    if fpr is not None:
        plt.figure(figsize=(6, 5))
        plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
        plt.plot([0, 1], [0, 1], linestyle="--", label="Random Guess")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC Curve")
        plt.legend()
        plt.tight_layout()
        plt.savefig("roc_curve.png", dpi=100, bbox_inches="tight")
        plt.close()
        print("ROC Curve plot saved to: roc_curve.png")
    print(f"\nROC AUC Score: {roc_auc if np.isfinite(roc_auc) else 'nan'}")


    # ==============================
    # 8. Write results to JSON and CSV
    # ==============================
    results_summary = {
        "overall": {
            "accuracy": float(_clamp_metric(accuracy)),
            "precision": float(_clamp_metric(precision)),
            "recall": float(_clamp_metric(recall)),
            "f1": float(_clamp_metric(f1)),
            "roc_auc": float(roc_auc) if np.isfinite(roc_auc) else None,
            "total_questions": int(len([q for q in EVALUATION_SET]))
        },
        "per_category": cat_summaries,
        "per_question": per_question
    }

    # write JSON
    with open("evaluation_results.json", "w", encoding="utf-8") as jf:
        json.dump(results_summary, jf, ensure_ascii=False, indent=2)
    print("\nSaved detailed results to: evaluation_results.json")

    # write CSV (flat per-question rows)
    import csv
    csv_fields = ["id", "category", "question", "chatbot_answer_preview", "score", "matched_keywords", "total_keywords", "prediction", "true_label"]
    with open("evaluation_results.csv", "w", newline='', encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=csv_fields)
        writer.writeheader()
        for row in per_question:
            writer.writerow({k: row.get(k, "") for k in csv_fields})
    print("Saved per-question CSV to: evaluation_results.csv")
