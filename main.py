
#problems
body_parts = ["Head","Skin","Heart","Digestion","Lungs","Eyes","Bones & Joints"]

# the symptoms for the problems
symptoms = {
           "Head" : [
            "Headache",
            "Migraine",
            "Dizziness",
            "Sinus Problem",
            "Dandruff"
        ],
        "Skin" : [
            "Pimples",
            "Acne",
            "Skin Allergy",
            "Tanning",
            "Eczema",
            "Dry Skin"
        ],
        "Heart" : [
            "Palpitations",
            "Chest Discomfort",
            "Irregular Heartbeat",
            "Unusual Fatigue",
            "Swelling"
        ],
        "Digestion" : [
            "Acidity",
            "Constipation",
            "Diarrhea",
            "Bloating",
            "Indigestion",
            "Stomach Pain"
        ],
        "Lungs" : [
            "Cough",
            "Wheezing",
            "Breathing Difficulty",
            "Chest Congestion",
            "Excess Mucus"
        ],
        "Eyes" : [
            "Red Eyes",
            "Dry Eyes",
            "Eye Itching",
            "Blurred Vision",
            "Eye Strain"
        ],
        "Bones & Joints" :  [
            "Back Pain",
            "Joint Pain",
            "Neck Pain",
            "Muscle Cramps",
            "Joint Swelling"
        ]
}

#Solution 

solutions = {

    # HEAD
    "Headache": [
        "Rest in a quiet room and drink enough water.",
        "Maintain regular sleep and avoid excessive screen time.",
        "Consult a doctor if headaches persist or become frequent."
    ],

    "Migraine": [
        "Rest in a dark and quiet room.",
        "Maintain regular sleep and identify possible migraine triggers.",
        "Consult a doctor for proper migraine evaluation and treatment."
    ],

    "Dizziness": [
        "Sit or lie down until the dizziness passes.",
        "Stay hydrated and avoid sudden changes in position.",
        "Consult a doctor if dizziness continues or occurs frequently."
    ],

    "Sinus Problem": [
        "Drink warm fluids and get sufficient rest.",
        "Try saline nasal spray to relieve nasal congestion.",
        "Consult a doctor if symptoms persist or worsen."
    ],

    "Dandruff": [
        "Wash your hair regularly with a gentle shampoo.",
        "Consider using an anti-dandruff shampoo as directed.",
        "Consult a dermatologist if dandruff persists or causes irritation."
    ],


    # SKIN
    "Pimples": [
        "Wash your face gently twice a day.",
        "Use non-comedogenic skincare products and avoid squeezing pimples.",
        "Consult a dermatologist if pimples persist or become painful."
    ],

    "Acne": [
        "Clean your skin gently and avoid touching your face frequently.",
        "Consider over-the-counter acne products with suitable ingredients.",
        "Consult a dermatologist for persistent or severe acne."
    ],

    "Skin Allergy": [
        "Stop using any recently introduced product that may be irritating your skin.",
        "Avoid scratching and use fragrance-free skincare products.",
        "Consult a doctor if the rash persists or spreads."
    ],

    "Tanning": [
        "Avoid prolonged direct sunlight.",
        "Use broad-spectrum SPF 30 or higher sunscreen.",
        "Consult a dermatologist if skin discoloration is unusual or persistent."
    ],

    "Eczema": [
        "Apply a fragrance-free moisturizer regularly.",
        "Avoid harsh soaps and other known skin irritants.",
        "Consult a dermatologist for persistent itching or inflammation."
    ],

    "Dry Skin": [
        "Apply moisturizer regularly, especially after bathing.",
        "Avoid hot showers and harsh soaps.",
        "Consult a dermatologist if dryness causes cracking or persistent irritation."
    ],


    # HEART
    "Palpitations": [
        "Stop strenuous activity and rest.",
        "Avoid excessive caffeine and monitor when palpitations occur.",
        "Seek medical evaluation for new or recurring palpitations."
    ],

    "Chest Discomfort": [
        "Stop physical activity and rest.",
        "Do not ignore unexplained chest discomfort; seek prompt medical assessment.",
        "Seek emergency medical help for chest pain or pressure, especially with sweating, breathlessness or faintness."
    ],

    "Irregular Heartbeat": [
        "Rest and avoid strenuous activity until assessed.",
        "Keep track of when the irregular heartbeat occurs.",
        "Arrange prompt medical evaluation; seek emergency help if accompanied by chest pain, fainting or breathing difficulty."
    ],

    "Unusual Fatigue": [
        "Get sufficient sleep and maintain regular meals.",
        "Stay hydrated and maintain a balanced diet.",
        "Consult a doctor if unexplained fatigue continues."
    ],

    "Swelling": [
        "Avoid prolonged sitting or standing.",
        "Monitor where the swelling occurs and whether it is increasing.",
        "Consult a doctor promptly to identify its cause."
    ],


    # DIGESTION
    "Acidity": [
        "Avoid large meals and identify foods that trigger symptoms.",
        "Avoid lying down immediately after eating.",
        "Consult a doctor if acidity is frequent or persistent."
    ],

    "Constipation": [
        "Drink sufficient water and eat fiber-rich foods.",
        "Include fruits, vegetables and regular physical activity in your routine.",
        "Consult a doctor if constipation persists or is accompanied by severe pain."
    ],

    "Diarrhea": [
        "Drink fluids and use oral rehydration solution (ORS) to prevent dehydration.",
        "Eat easily tolerated foods and continue replacing lost fluids.",
        "Seek medical attention for blood in stool, severe dehydration, high fever or persistent diarrhea."
    ],

    "Bloating": [
        "Eat slowly and avoid overeating.",
        "Identify foods that cause gas and reduce carbonated drinks.",
        "Consult a doctor if bloating is persistent or accompanied by severe pain."
    ],

    "Indigestion": [
        "Eat smaller meals and avoid overeating.",
        "Limit foods that trigger discomfort and avoid lying down after meals.",
        "Consult a doctor if indigestion occurs frequently."
    ],

    "Stomach Pain": [
        "Rest and monitor the location and severity of the pain.",
        "Drink fluids and avoid foods that worsen the discomfort.",
        "Seek medical evaluation for persistent or worsening pain; severe sudden pain requires emergency care."
    ],


    # LUNGS
    "Cough": [
        "Drink warm fluids to soothe your throat.",
        "Avoid smoke, dust and other respiratory irritants.",
        "Consult a doctor if the cough persists, worsens or is accompanied by fever or blood."
    ],

    "Wheezing": [
        "Avoid smoke, dust and other known triggers.",
        "Follow your prescribed inhaler or asthma action plan if you have one.",
        "Seek medical evaluation for new or recurring wheezing; severe breathing difficulty requires emergency help."
    ],

    "Breathing Difficulty": [
        "Stop activity and sit upright in a comfortable position.",
        "Follow your prescribed emergency breathing treatment if you have one.",
        "Seek emergency medical help for new or significant breathing difficulty."
    ],

    "Chest Congestion": [
        "Drink enough fluids and get adequate rest.",
        "Avoid smoking and exposure to polluted air.",
        "Consult a doctor if congestion worsens or breathing becomes difficult."
    ],

    "Excess Mucus": [
        "Drink enough water to help maintain hydration.",
        "Avoid smoke and other respiratory irritants.",
        "Consult a doctor if excessive mucus persists or contains blood."
    ],


    # EYES
    "Red Eyes": [
        "Avoid rubbing your eyes.",
        "Use a clean cool compress and avoid potential irritants.",
        "Consult an eye doctor if redness persists, is painful or affects vision."
    ],

    "Dry Eyes": [
        "Take regular breaks from screens.",
        "Consider preservative-free lubricating eye drops.",
        "Consult an eye doctor if dryness continues."
    ],

    "Eye Itching": [
        "Avoid rubbing your eyes.",
        "Use a clean cool compress.",
        "Consult an eye doctor if itching persists or is accompanied by pain or discharge."
    ],

    "Blurred Vision": [
        "Stop activities that require clear vision, such as driving.",
        "Arrange an eye examination promptly.",
        "Seek emergency medical help for sudden blurred vision or vision loss."
    ],

    "Eye Strain": [
        "Take regular breaks using the 20-20-20 rule.",
        "Adjust screen brightness and maintain a comfortable viewing distance.",
        "Consult an eye doctor if eye strain continues."
    ],


    # BONES & JOINTS
    "Back Pain": [
        "Avoid activities that worsen the pain while staying gently active.",
        "Use a warm or cold compress and maintain good posture.",
        "Consult a doctor if pain persists or becomes severe."
    ],

    "Joint Pain": [
        "Rest the affected joint and avoid activities that worsen pain.",
        "Try a cold compress for swelling and avoid overloading the joint.",
        "Consult a doctor if joint pain persists or limits movement."
    ],

    "Neck Pain": [
        "Avoid sudden neck movements and maintain comfortable posture.",
        "Try gentle movement and a warm compress.",
        "Consult a doctor if neck pain persists or is accompanied by weakness or numbness."
    ],

    "Muscle Cramps": [
        "Gently stretch the affected muscle.",
        "Stay hydrated and avoid excessive muscle strain.",
        "Consult a doctor if cramps occur frequently or are severe."
    ],

    "Joint Swelling": [
        "Rest the affected joint and avoid putting excessive weight on it.",
        "Apply a cold compress wrapped in a cloth.",
        "Seek medical evaluation, especially if the joint is hot, red, very painful or accompanied by fever."
    ]
}


def welcome():
    print("\n================================")
    print("       HEALTHCARE CHATBOT")
    print("================================")
    print("Welcome! I am your health assistant.")
    print("I can provide general health information.")
    print("--------------------------------")

def take_body_part():
    print("seler the Body part where you have problem")
    for i in range(0,len(body_parts)):
        print(f"{i+1} for {body_parts[i]}")
    val=int(input("enter : "))
    return val-1

def select_symptom(b):
    print(f"select the symptom for {body_parts[b]}")
    for i in range(0,len(symptoms[body_parts[b]])):
        print(f"{i+1} for {symptoms[body_parts[b]][i]}")
    val=int(input("enter : "))
    return symptoms[body_parts[b]][val-1]

def take_duration():
    print("from when you are facing this problem")
    print("1 for 1-60 days")
    print("2 for 2-6 months")
    print("3 for more that one year")
    val=int(input("enter : "))
    return val

def take_Severity():
    print("selece the Severity of the problem")
    print("1 for Mild")
    print("2 for Moderate")
    print("3 for Severe")
    val=int(input("enter : "))
    return val

def display_solution(symptom, result):
    print("\n========== SUGGESTION ==========")
    print("Reported problem:", symptom)
    print("Suggestion:")
    print(solutions[symptom][result - 1])
    print("================================")

def analyze(age,d,s):
    if(age<18):
        a=1
    elif(age<40):
        a=2
    else:
        a=3

    val=round((a*0.2)+(d*0.4)+(s*0.4))
    return val


# star .............................................................................................

welcome()
b=take_body_part()
sym=select_symptom(b)
age=int(input("Enter your age : "))
duration=take_duration()
Severity=take_Severity()
cal=analyze(age,duration,Severity)
display_solution(sym,cal)
