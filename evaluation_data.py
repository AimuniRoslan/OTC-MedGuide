# evaluation_data.py
# Category A: Symptom-to-OTC Matching (10 Questions)
# Each item contains:
# - id: question number for easy reference
# - question: what is asked to the chatbot
# - ground_truth: factual statements expected to appear in a correct answer

EVALUATION_SET = [
    {
        "id": 1,
        "question": "What OTC medicine is good for a mild headache?",
        "ground_truth": [
            "Paracetamol (acetaminophen) is an OTC analgesic commonly used for mild headache relief",
            "Ibuprofen is an OTC NSAID effective for mild headache and tension-type headache",
            "Aspirin is an OTC analgesic that can relieve mild headache in adults",
            "Naproxen sodium is an OTC NSAID that provides longer-lasting headache relief",
            "Combination analgesics containing caffeine and paracetamol are available OTC for headache relief",
            "Paracetamol is preferred for individuals with sensitive stomachs compared to NSAIDs",
            "Ibuprofen reduces both pain and inflammation associated with mild headache",
            "Aspirin should not be used in children due to risk of Reye’s syndrome"
        ]
    },
    {
        "id": 2,
        "question": "I have a fever of 38°C. What can I take?",
        "ground_truth": [
            "Paracetamol (acetaminophen) is an OTC antipyretic used to reduce fever",
            "Ibuprofen is an OTC NSAID that lowers fever and relieves associated aches",
            "Naproxen sodium is an OTC NSAID that can reduce fever and inflammation",
            "Aspirin can reduce fever in adults but is not recommended for children",
            "Paracetamol is generally considered safe for fever management at recommended doses",
            "Ibuprofen provides both fever reduction and anti-inflammatory effects"
        ]
    },
    {
        "id": 3,
        "question": "Sore throat remedies available over-the-counter?",
        "ground_truth": [
            "Paracetamol (acetaminophen) is an OTC analgesic that relieves sore throat pain",
            "Ibuprofen is an OTC NSAID that reduces sore throat pain and inflammation",
            "Aspirin can relieve sore throat pain in adults",
            "Benzocaine lozenges are OTC local anesthetics that numb sore throat pain",
            "Phenol-based throat sprays are OTC products that provide temporary sore throat relief",
            "Dyclonine lozenges are OTC anesthetic lozenges for sore throat",
            "Menthol lozenges are OTC products that provide cooling relief for sore throat discomfort",
            "Chloraseptic sprays containing phenol are widely available OTC for sore throat relief"
        ]
    },
    {
        "id": 4,
        "question": "I have a runny nose and sneezing. Recommend a drug.",
        "ground_truth": [
            "Loratadine is a non-drowsy OTC antihistamine used for runny nose and sneezing",
            "Cetirizine is an OTC antihistamine that relieves sneezing and runny nose",
            "Fexofenadine is a non-sedating OTC antihistamine used for hay fever symptoms",
            "Chlorpheniramine is a first-generation OTC antihistamine that reduces sneezing and rhinorrhea",
            "Diphenhydramine is an OTC antihistamine that relieves nasal allergy symptoms but may cause drowsiness"
        ]
    },
    {
        "id": 5,
        "question": "Stomach upset after dinner - any OTC options?",
        "ground_truth": [
            "Antacids such as calcium carbonate are OTC medicines that relieve stomach upset and heartburn",
            "Simethicone is an OTC anti-gas medicine that reduces bloating and discomfort",
            "Bismuth subsalicylate is an OTC medicine that treats indigestion, nausea, and upset stomach",
            "Famotidine is an OTC H2 blocker that reduces stomach acid and relieves heartburn",
            "Omeprazole is an OTC proton pump inhibitor that reduces stomach acid for frequent indigestion"
        ]
    },
    {
        "id": 6,
        "question": "My child has mild cough - what should I give?",
        "ground_truth": [
            "Children’s cough syrups containing dextromethorphan are OTC cough suppressants for dry cough",
            "Guaifenesin is an OTC expectorant that helps loosen mucus in children",
            "Honey-based OTC cough syrups are safe for children above 1 year old",
            "Diphenhydramine is an OTC antihistamine sometimes included in pediatric cough medicines",
            "Always check age-specific dosing instructions before giving OTC cough medicine to children"
        ]
    },
    {
        "id": 7,
        "question": "Muscle pain from exercise - what OTC works best?",
        "ground_truth": [
            "Ibuprofen is an OTC NSAID that relieves muscle pain and reduces inflammation",
            "Paracetamol (acetaminophen) is an OTC analgesic for mild muscle pain",
            "Naproxen sodium is an OTC NSAID that provides longer-lasting relief for muscle pain",
            "Topical analgesic creams containing menthol are OTC products for localized muscle pain relief",
            "Topical diclofenac gel is an OTC NSAID used for muscle pain and inflammation"
        ]
    },
    {
        "id": 8,
        "question": "Allergic skin rash - what can I use?",
        "ground_truth": [
            "Hydrocortisone 1% cream is an OTC topical corticosteroid that reduces itching and redness from allergic rash",
            "Calamine lotion is an OTC product that soothes irritated skin and allergic rash",
            "Oral antihistamines such as loratadine are OTC medicines that relieve allergic skin reactions",
            "Cetirizine is an OTC antihistamine that reduces itching from allergic rash",
            "Diphenhydramine cream is an OTC topical antihistamine that reduces itching from allergic rash"
        ]
    },
    {
        "id": 9,
        "question": "Mild insomnia - any safe OTC medicines?",
        "ground_truth": [
            "Diphenhydramine is an OTC antihistamine used as a sleep aid for mild insomnia",
            "Doxylamine is an OTC antihistamine used for short-term insomnia",
            "Melatonin supplements are available OTC to help regulate sleep cycles",
            "Combination nighttime pain relievers with diphenhydramine are OTC products used for insomnia with pain",
            "OTC antihistamine sleep aids may cause next-day drowsiness"
        ]
    },
    {
        "id": 10,
        "question": "Motion sickness during travel - suggest options.",
        "ground_truth": [
            "Dimenhydrinate is an OTC antihistamine used to prevent and treat motion sickness",
            "Meclizine is an OTC antihistamine effective for motion sickness prevention",
            "Diphenhydramine is an OTC antihistamine that can reduce motion sickness symptoms",
            "Ginger capsules are available OTC and may help reduce nausea from motion sickness",
            "Antihistamine-based OTC medicines are commonly used for motion sickness prevention"
        ]
    },
# Category B: Dosage Accuracy (10 Questions)
    {
        "id": 11,
        "question": "How much acetaminophen can an adult take for a headache?",
        "ground_truth": [
            "The usual adult dose of acetaminophen (paracetamol) is 500 mg to 1000 mg every 4 to 6 hours as needed",
            "The maximum daily dose of acetaminophen for adults is 4000 mg in 24 hours",
            "Acetaminophen should not be taken more frequently than every 4 hours",
            "Extended-release acetaminophen tablets may be taken every 8 hours",
            "Exceeding 4000 mg per day of acetaminophen can cause severe liver damage",
            "Acetaminophen is commonly used for headache relief at doses of 500 mg per tablet"
        ]
    },
    {
        "id": 12,
        "question": "Maximum ibuprofen dose in 24 hours for adults?",
        "ground_truth": [
            "The usual adult dose of ibuprofen is 200 mg to 400 mg every 4 to 6 hours as needed",
            "The maximum OTC ibuprofen dose for adults is 1200 mg in 24 hours",
            "Prescription doses of ibuprofen can be higher, but OTC limit is 1200 mg per day",
            "Ibuprofen should not be taken more frequently than every 4 hours",
            "Exceeding the maximum OTC dose of ibuprofen increases risk of stomach irritation and kidney damage"
        ]
    },
    {
        "id": 13,
        "question": "Safe diphenhydramine dose for a 5-year-old?",
        "ground_truth": [
            "The usual pediatric dose of diphenhydramine for a 5-year-old is 12.5 mg every 4 to 6 hours as needed",
            "The maximum daily dose of diphenhydramine for children aged 2 to 6 years is 75 mg in 24 hours",
            "Diphenhydramine liquid formulations are commonly used for children, with dosing based on weight and age",
            "Diphenhydramine should not be given more than 6 times in 24 hours",
            "Always use a calibrated dosing device for liquid diphenhydramine in children"
        ]
    },
    {
        "id": 14,
        "question": "Naproxen OTC dose for a 12-year-old?",
        "ground_truth": [
            "Naproxen sodium is generally not recommended for children under 12 years old without medical advice",
            "For children aged 12 years and older, the usual OTC dose is 220 mg every 8 to 12 hours",
            "The maximum OTC naproxen sodium dose for adolescents is 660 mg in 24 hours",
            "Naproxen should be taken with food to reduce stomach irritation",
            "Children under 12 should not use OTC naproxen unless directed by a healthcare professional"
        ]
    },
    {
        "id": 15,
        "question": "Aspirin dose for heart protection in adults?",
        "ground_truth": [
            "The typical OTC aspirin dose for heart protection is 81 mg once daily (low-dose aspirin)",
            "Low-dose aspirin (baby aspirin) is commonly used for cardiovascular protection",
            "Some adults may take 325 mg aspirin daily for heart protection if directed by a doctor",
            "Aspirin should be taken with food to reduce stomach irritation",
            "Aspirin is not recommended for routine heart protection in individuals at risk of bleeding without medical advice"
        ]
    },
    {
        "id": 16,
        "question": "Loperamide dose for diarrhea in adults and children?",
        "ground_truth": [
            "The usual adult dose of loperamide is 4 mg initially, followed by 2 mg after each loose stool",
            "The maximum OTC loperamide dose for adults is 8 mg in 24 hours",
            "For children aged 6 to 12 years, the typical dose is 2 mg after the first loose stool, then 1 mg after subsequent stools",
            "Children under 6 years should not use OTC loperamide unless directed by a doctor",
            "Exceeding the maximum dose of loperamide can cause serious heart rhythm problems"
        ]
    },
    {
        "id": 17,
        "question": "Omeprazole 20mg frequency for heartburn?",
        "ground_truth": [
            "The usual OTC dose of omeprazole for heartburn is 20 mg once daily",
            "Omeprazole should be taken before a meal, preferably in the morning",
            "OTC omeprazole is intended for a 14-day course of treatment",
            "Omeprazole should not be taken more than once daily at the OTC strength",
            "If symptoms persist after 14 days of omeprazole, medical advice should be sought"
        ]
    },
    {
        "id": 18,
        "question": "Loratadine dosage for a 4-year-old child?",
        "ground_truth": [
            "The usual loratadine dose for children aged 2 to 5 years is 5 mg once daily",
            "Loratadine is available as a syrup formulation for children",
            "Children aged 6 years and older can take 10 mg once daily",
            "Loratadine is a non-drowsy antihistamine suitable for pediatric allergy relief",
            "Do not exceed 5 mg daily loratadine in children under 6 years old"
        ]
    },
    {
        "id": 19,
        "question": "Famotidine OTC dosage for adult with frequent heartburn?",
        "ground_truth": [
            "The usual OTC dose of famotidine for adults is 10 mg to 20 mg once or twice daily",
            "Famotidine can be taken before meals to prevent heartburn",
            "The maximum OTC famotidine dose is 40 mg in 24 hours",
            "Famotidine is an H2 blocker that reduces stomach acid",
            "Famotidine should not be used for more than 14 days without medical advice"
        ]
    },
    {
        "id": 20,
        "question": "Dextromethorphan dosing for a 7-year-old?",
        "ground_truth": [
            "The usual dextromethorphan dose for children aged 6 to 12 years is 5 mg to 10 mg every 4 hours as needed",
            "The maximum daily dose of dextromethorphan for children aged 6 to 12 years is 60 mg in 24 hours",
            "Dextromethorphan is available in liquid formulations for pediatric use",
            "Do not exceed recommended dosing frequency for dextromethorphan in children",
            "Always use a calibrated dosing device for liquid dextromethorphan in children"
        ]
    },
# Category C: Drug Comparisons (10 Questions)
    {
        "id": 21,
        "question": "Acetaminophen vs ibuprofen – which is better for headache?",
        "ground_truth": [
            "Acetaminophen (paracetamol) is effective for mild to moderate headache relief",
            "Ibuprofen is effective for headache relief and also reduces inflammation",
            "Acetaminophen is preferred for individuals with stomach sensitivity or risk of ulcers",
            "Ibuprofen may be more effective for headaches associated with muscle tension or inflammation",
            "Both acetaminophen and ibuprofen are widely available OTC analgesics for headache",
            "Acetaminophen is safer for individuals with kidney disease compared to NSAIDs",
            "Ibuprofen provides dual benefits of pain relief and anti-inflammatory action"
        ]
    },
    {
        "id": 22,
        "question": "Loratadine vs cetirizine – differences?",
        "ground_truth": [
            "Loratadine is a non-drowsy OTC antihistamine used for allergy symptoms",
            "Cetirizine is an OTC antihistamine that may cause mild drowsiness in some users",
            "Both loratadine and cetirizine relieve sneezing, runny nose, and itchy eyes",
            "Cetirizine may provide faster onset of symptom relief compared to loratadine",
            "Loratadine is preferred for daytime use due to minimal sedation",
            "Cetirizine is sometimes more effective for severe allergy symptoms",
            "Both are second-generation antihistamines available OTC"
        ]
    },
    {
        "id": 23,
        "question": "Diphenhydramine vs loratadine – daytime use?",
        "ground_truth": [
            "Diphenhydramine is a first-generation OTC antihistamine that causes significant drowsiness",
            "Loratadine is a non-drowsy OTC antihistamine suitable for daytime use",
            "Diphenhydramine is often used as a nighttime sleep aid due to sedative effects",
            "Loratadine is preferred for daytime allergy relief because it does not impair alertness",
            "Diphenhydramine is not recommended for daytime use when alertness is required",
            "Both are available OTC but differ in sedation profile"
        ]
    },
    {
        "id": 24,
        "question": "Ibuprofen vs naproxen – which lasts longer?",
        "ground_truth": [
            "Ibuprofen is an OTC NSAID with a duration of action of about 4 to 6 hours",
            "Naproxen sodium is an OTC NSAID with a longer duration of action, about 8 to 12 hours",
            "Naproxen provides longer-lasting pain relief compared to ibuprofen",
            "Ibuprofen may be preferred for short-term pain relief due to shorter half-life",
            "Both ibuprofen and naproxen are effective OTC NSAIDs for pain and inflammation"
        ]
    },
    {
        "id": 25,
        "question": "Omeprazole vs famotidine – which is more effective for acid reflux?",
        "ground_truth": [
            "Omeprazole is an OTC proton pump inhibitor that provides stronger and longer-lasting acid suppression",
            "Famotidine is an OTC H2 blocker that reduces stomach acid but is less potent than omeprazole",
            "Omeprazole is more effective for frequent heartburn and GERD symptoms",
            "Famotidine provides faster relief but shorter duration compared to omeprazole",
            "Both omeprazole and famotidine are available OTC for acid reflux management"
        ]
    },
    {
        "id": 26,
        "question": "Loperamide vs bismuth subsalicylate – best for diarrhea?",
        "ground_truth": [
            "Loperamide is an OTC antidiarrheal that slows intestinal movement and reduces stool frequency",
            "Bismuth subsalicylate is an OTC medicine that treats diarrhea and also relieves nausea and upset stomach",
            "Loperamide is more effective for controlling acute non-infectious diarrhea",
            "Bismuth subsalicylate provides broader symptom relief including indigestion and stomach upset",
            "Both loperamide and bismuth subsalicylate are available OTC for diarrhea treatment"
        ]
    },
    {
        "id": 27,
        "question": "Aspirin vs ibuprofen – which is safer for stomach?",
        "ground_truth": [
            "Aspirin is more likely to cause stomach irritation and ulcers compared to ibuprofen",
            "Ibuprofen is generally considered safer for the stomach at OTC doses than aspirin",
            "Both aspirin and ibuprofen can cause gastrointestinal side effects",
            "Aspirin should be avoided in individuals with a history of stomach ulcers",
            "Ibuprofen is preferred over aspirin for pain relief in patients with sensitive stomachs"
        ]
    },
    {
        "id": 28,
        "question": "Acetaminophen vs aspirin – which is better for fever?",
        "ground_truth": [
            "Acetaminophen (paracetamol) is commonly preferred for reducing fever",
            "Aspirin can reduce fever but is not recommended for children due to risk of Reye’s syndrome",
            "Acetaminophen is safer for fever management in both adults and children",
            "Aspirin is used for fever in adults but less commonly than acetaminophen",
            "Both acetaminophen and aspirin are available OTC antipyretics"
        ]
    },
    {
        "id": 29,
        "question": "Vitamin C vs zinc – which helps cold faster?",
        "ground_truth": [
            "Vitamin C is an OTC supplement that may reduce the duration of cold symptoms",
            "Zinc lozenges are OTC products that may shorten the duration of colds if taken early",
            "Evidence suggests zinc may be more effective than vitamin C in reducing cold duration",
            "Vitamin C supports immune function but has limited effect on cold recovery speed",
            "Both vitamin C and zinc are widely available OTC supplements for cold support"
        ]
    },
    {
        "id": 30,
        "question": "Cetirizine vs diphenhydramine – drowsiness comparison?",
        "ground_truth": [
            "Cetirizine is a second-generation OTC antihistamine that may cause mild drowsiness in some users",
            "Diphenhydramine is a first-generation OTC antihistamine that causes significant drowsiness",
            "Cetirizine is generally suitable for daytime use due to lower sedation risk",
            "Diphenhydramine is often used as a nighttime sleep aid due to sedative effects",
            "Diphenhydramine is not recommended for daytime use when alertness is required"
        ]
    },
# Category D: Safety / Warnings / Contraindications (10 Questions)
    {
        "id": 31,
        "question": "Can pregnant women take ibuprofen?",
        "ground_truth": [
            "Ibuprofen is generally not recommended during pregnancy, especially in the third trimester",
            "Use of ibuprofen in late pregnancy may cause premature closure of the fetal ductus arteriosus",
            "Ibuprofen may increase risk of complications such as low amniotic fluid and delayed labor",
            "Paracetamol (acetaminophen) is generally considered safer for pain relief during pregnancy",
            "Pregnant women should consult a healthcare provider before using any OTC NSAIDs"
        ]
    },
    {
        "id": 32,
        "question": "Can children under 6 take diphenhydramine?",
        "ground_truth": [
            "Diphenhydramine is not recommended for children under 6 years old without medical supervision",
            "Diphenhydramine may cause excessive sedation or paradoxical excitation in young children",
            "OTC labeling advises against use of diphenhydramine in children under 6 for cough and cold symptoms",
            "Safer alternatives such as loratadine or cetirizine are preferred for allergy relief in young children",
            "Always consult a pediatrician before giving diphenhydramine to children under 6"
        ]
    },
    {
        "id": 33,
        "question": "Interactions of acetaminophen with other drugs?",
        "ground_truth": [
            "Acetaminophen can interact with alcohol, increasing risk of liver damage",
            "Concurrent use of acetaminophen with other acetaminophen-containing products may lead to overdose",
            "Acetaminophen may interact with warfarin, increasing risk of bleeding with prolonged use",
            "Combination cold and flu OTC products often contain acetaminophen, raising risk of duplication",
            "Always check labels to avoid exceeding the maximum daily dose of acetaminophen"
        ]
    },
    {
        "id": 34,
        "question": "Can aspirin be given to teenagers with flu?",
        "ground_truth": [
            "Aspirin should not be given to teenagers or children with flu due to risk of Reye’s syndrome",
            "Reye’s syndrome is a rare but serious condition linked to aspirin use in viral illnesses",
            "Safer alternatives such as acetaminophen or ibuprofen are recommended for fever in teenagers",
            "OTC labeling warns against aspirin use in children and adolescents with viral infections",
            "Aspirin is contraindicated in pediatric flu and chickenpox cases"
        ]
    },
    {
        "id": 35,
        "question": "Loperamide side effects to watch for?",
        "ground_truth": [
            "Loperamide may cause constipation as a common side effect",
            "Dizziness and drowsiness can occur with loperamide use",
            "Serious side effects include irregular heartbeat and cardiac arrhythmias if overdosed",
            "Abdominal cramps and bloating are possible side effects of loperamide",
            "Loperamide should not be used in children under 6 without medical advice"
        ]
    },
    {
        "id": 36,
        "question": "Omeprazole long-term safety?",
        "ground_truth": [
            "Long-term use of omeprazole may increase risk of vitamin B12 deficiency",
            "Prolonged omeprazole use may lead to low magnesium levels",
            "Chronic use of omeprazole may increase risk of bone fractures",
            "Omeprazole long-term use may increase risk of gastrointestinal infections such as C. difficile",
            "OTC omeprazole is intended for short-term use, typically 14 days"
        ]
    },
    {
        "id": 37,
        "question": "Loratadine in patients with kidney issues?",
        "ground_truth": [
            "Loratadine is generally safe but should be used with caution in patients with severe kidney impairment",
            "Dose adjustment may be required for loratadine in patients with renal dysfunction",
            "Cetirizine and loratadine both require caution in kidney disease due to slower clearance",
            "OTC labeling advises consulting a healthcare provider before use in patients with kidney problems",
            "Non-sedating antihistamines like loratadine are preferred but require medical guidance in renal impairment"
        ]
    },
    {
        "id": 38,
        "question": "Naproxen for someone with stomach ulcers?",
        "ground_truth": [
            "Naproxen should be avoided in individuals with active stomach ulcers",
            "NSAIDs like naproxen increase risk of gastrointestinal bleeding and ulcer worsening",
            "Paracetamol (acetaminophen) is a safer OTC alternative for pain relief in patients with ulcers",
            "OTC labeling warns against naproxen use in people with history of stomach ulcers",
            "Naproxen should be taken with food if used, but is contraindicated in active ulcer disease"
        ]
    },
    {
        "id": 39,
        "question": "Supplements safe during pregnancy?",
        "ground_truth": [
            "Prenatal vitamins containing folic acid are safe and recommended during pregnancy",
            "Iron supplements are commonly used during pregnancy to prevent anemia",
            "Calcium supplements are safe and support bone health during pregnancy",
            "Vitamin D supplements are safe and support maternal and fetal bone development",
            "High-dose vitamin A supplements should be avoided during pregnancy due to risk of birth defects"
        ]
    },
    {
        "id": 40,
        "question": "Dextromethorphan in children under 4 years?",
        "ground_truth": [
            "Dextromethorphan is not recommended for children under 4 years old",
            "OTC labeling advises against use of cough suppressants in children under 4",
            "Dextromethorphan may cause side effects such as drowsiness or agitation in young children",
            "Safer alternatives include honey-based remedies for children over 1 year old",
            "Always consult a pediatrician before giving dextromethorphan to young children"
        ]
    },
# Category E: Knowledge / Mechanism / General Info (10 Questions)
    {
        "id": 41,
        "question": "How does acetaminophen reduce fever?",
        "ground_truth": [
            "Acetaminophen reduces fever by inhibiting prostaglandin synthesis in the hypothalamus",
            "It acts centrally on the brain’s thermoregulatory center to lower body temperature",
            "Unlike NSAIDs, acetaminophen has minimal anti-inflammatory activity",
            "Acetaminophen is an OTC antipyretic commonly used for fever reduction",
            "It is considered safe at recommended doses but overdose can cause liver toxicity"
        ]
    },
    {
        "id": 42,
        "question": "Why is ibuprofen anti-inflammatory?",
        "ground_truth": [
            "Ibuprofen is an NSAID that works by inhibiting cyclooxygenase (COX) enzymes",
            "Inhibition of COX enzymes reduces prostaglandin production, lowering inflammation",
            "Ibuprofen provides both pain relief and anti-inflammatory effects",
            "It is available OTC for conditions such as headache, muscle pain, and arthritis",
            "Ibuprofen’s anti-inflammatory action makes it more effective than acetaminophen for swelling"
        ]
    },
    {
        "id": 43,
        "question": "How do antihistamines work for allergies?",
        "ground_truth": [
            "Antihistamines block histamine H1 receptors, preventing histamine from binding",
            "This reduces allergy symptoms such as sneezing, runny nose, and itchy eyes",
            "OTC antihistamines include loratadine, cetirizine, fexofenadine, and diphenhydramine",
            "First-generation antihistamines like diphenhydramine cause sedation",
            "Second-generation antihistamines like loratadine are non-drowsy and suitable for daytime use"
        ]
    },
    {
        "id": 44,
        "question": "Difference between H1 and H2 blockers?",
        "ground_truth": [
            "H1 blockers are antihistamines used for allergy symptoms such as sneezing and itching",
            "Examples of OTC H1 blockers include loratadine, cetirizine, and diphenhydramine",
            "H2 blockers reduce stomach acid by blocking histamine H2 receptors in the stomach lining",
            "Examples of OTC H2 blockers include famotidine",
            "H1 blockers target allergic reactions, while H2 blockers target acid-related conditions"
        ]
    },
    {
        "id": 45,
        "question": "How does loperamide stop diarrhea?",
        "ground_truth": [
            "Loperamide slows intestinal motility by acting on opioid receptors in the gut wall",
            "This increases transit time and allows more water absorption from stool",
            "Loperamide reduces stool frequency and improves stool consistency",
            "It is an OTC antidiarrheal used for acute non-infectious diarrhea",
            "Loperamide does not treat the underlying cause of diarrhea but controls symptoms"

        ]
    },
    {
        "id": 46,
        "question": "Mechanism of omeprazole for acid reduction?",
        "ground_truth": [
            "Omeprazole is a proton pump inhibitor that blocks the H+/K+ ATPase enzyme in stomach lining",
            "This prevents final step of gastric acid secretion, reducing stomach acid production",
            "Omeprazole provides longer-lasting acid suppression compared to H2 blockers",
            "It is available OTC for frequent heartburn and GERD",
            "Omeprazole is usually taken once daily before meals for best effect"
        ]
    },
    {
        "id": 47,
        "question": "Difference between OTC and prescription doses?",
        "ground_truth": [
            "OTC doses are lower and intended for short-term use without medical supervision",
            "Prescription doses are higher and used for more severe or chronic conditions",
            "For example, OTC ibuprofen maximum is 1200 mg/day, while prescription allows up to 3200 mg/day",
            "OTC omeprazole is 20 mg once daily, while prescription doses may be higher or longer duration",
            "OTC labeling includes strict duration limits, while prescription use is guided by a physician"
        ]
    },
    {
        "id": 48,
        "question": "Why avoid aspirin in children with viral infections?",
        "ground_truth": [
            "Aspirin use in children with viral infections is linked to Reye’s syndrome",
            "Reye’s syndrome is a rare but serious condition causing liver and brain damage",
            "OTC labeling warns against aspirin use in children and teenagers with flu or chickenpox",
            "Safer alternatives for fever in children include acetaminophen and ibuprofen",
            "Aspirin is contraindicated in pediatric viral illnesses due to safety risks"
        ]
    },
    {
        "id": 49,
        "question": "How to take antacids safely?",
        "ground_truth": [
            "Antacids should be taken as needed for heartburn or indigestion",
            "Common OTC antacids include calcium carbonate and magnesium hydroxide",
            "Antacids should not be taken in excessive amounts to avoid electrolyte imbalance",
            "They may interfere with absorption of other medications if taken simultaneously",
            "Antacids are generally safe but should be used according to package instructions"

        ]
    },
    {
        "id": 50,
        "question": "How to store OTC drugs safely at home?",
        "ground_truth": [
            "OTC drugs should be stored in a cool, dry place away from direct sunlight",
            "Medicines should be kept out of reach of children and pets",
            "Store drugs in their original packaging with labels intact",
            "Avoid storing medicines in bathrooms due to humidity",
            "Check expiration dates regularly and discard expired OTC drugs safely"
        ]
    }
]

