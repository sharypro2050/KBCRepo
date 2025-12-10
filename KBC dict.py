store = {
    "questions": [
        "What is the capital of Australia?",
        "Which planet is known as the Red Planet?",
        "Who is the author of the Harry Potter series?",
        "Which continent is the Sahara Desert located on?",
        "What is the largest ocean in the world?",
        "Which country is famous for the Taj Mahal?",
        "What is the tallest mountain in the world?",
        "Which country hosted the 2016 Summer Olympics?",
        "Who invented the light bulb?",
        "Which is the smallest country in the world?",
        "Which river is the longest in the world?",
        "In which country would you find the Great Barrier Reef?",
        "Which language is primarily spoken in Brazil?",
        "What is the currency of Japan?",
        "Which country is known as the Land of the Rising Sun?",
        "Which city is known as the 'City of Love'?"
    ],
    "options": [
        ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"],
        ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        ["A) J.R.R. Tolkien", "B) J.K. Rowling", "C) George R.R. Martin", "D) Suzanne Collins"],
        ["A) Asia", "B) Africa", "C) Australia", "D) South America"],
        ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        ["A) Pakistan", "B) India", "C) Bangladesh", "D) Afghanistan"],
        ["A) K2", "B) Kangchenjunga", "C) Mount Everest", "D) Lhotse"],
        ["A) China", "B) Brazil", "C) United Kingdom", "D) Australia"],
        ["A) Alexander Graham Bell", "B) Nikola Tesla", "C) Thomas Edison", "D) Michael Faraday"],
        ["A) Monaco", "B) Nauru", "C) Vatican City", "D) San Marino"],
        ["A) Amazon River", "B) Nile River", "C) Yangtze River", "D) Mississippi River"],
        ["A) Philippines", "B) Australia", "C) Indonesia", "D) Fiji"],
        ["A) Spanish", "B) Portuguese", "C) French", "D) English"],
        ["A) Yen", "B) Won", "C) Peso", "D) Ringgit"],
        ["A) China", "B) South Korea", "C) Japan", "D) Thailand"],
        ["A) Venice", "B) Paris", "C) Rome", "D) Prague"]
    ],
    "answers": ["C","B","B","B","D","B","C","B","C","C","B","B","B","A","C","B"],
    "prize": [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 500000, 7500000, 10000000]}
track = 0
total_prize = 0
for que in range(len(store['questions'])):
    print((store['questions'][que]))
    for opt in range(4):
        print(store['options'][que][opt])
    user_input = input("Type your answer (A,B,C or D) here: ").upper()
    
    while user_input !='A'and user_input !='B' and user_input !='C' and user_input !='D':
        print("Invalid input! Type only A, B , C or D")
        user_input = input("Enter your answer here: ").upper()
    if user_input == store['answers'][que]:
        track +=1
        total_prize = store['prize'][que]
        print('------------------------------------------------------------------------------------------------')
            
    else: 
        print("Wrong answer You have won Rs.", total_prize)
        break 
print(f'You have answered {track}/16 questions correctly\nYour total winning amount is NRs. {total_prize}')       