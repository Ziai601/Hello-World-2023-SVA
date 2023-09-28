def determine_zodiac(year):
    zodiacs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return zodiacs[(year - 1960) % 12]

def get_fortune(zodiac):
    fortunes = {
        "Rat": "Rats are known for their intelligence and adaptability. This year, focus on new opportunities and be ready to seize them.",
        "Ox": "Oxen are known for their diligence and dependability. This year, your hard work will pay off, but remember to also take time for yourself.",
        "Tiger": "Tigers are known for their courage and passion. This year, embrace your adventurous spirit and pursue your dreams with confidence.",
        "Rabbit": "Rabbits are known for their gentleness and diplomacy. This year, your ability to navigate relationships will be a key factor in your success.",
        "Dragon": "Dragons are known for their strength and ambition. This year, channel your inner fire and pursue your goals with determination.",
        "Snake": "Snakes are known for their wisdom and intuition. This year, trust your instincts and be open to transformation.",
        "Horse": "Horses are known for their independence and energy. This year, harness your vitality and explore new horizons.",
        "Goat": "Goats are known for their creativity and kindness. This year, let your imagination flourish and spread positivity around you.",
        "Monkey": "Monkeys are known for their wit and adaptability. This year, embrace change and use your intelligence to overcome challenges.",
        "Rooster": "Roosters are known for their confidence and honesty. This year, stand tall and be true to yourself in all situations.",
        "Dog": "Dogs are known for their loyalty and reliability. This year, your steadfastness will be a source of strength for you and those around you.",
        "Pig": "Pigs are known for their generosity and optimism. This year, focus on building meaningful connections and enjoy the abundance life has to offer."
    }
    return fortunes.get(zodiac, "Invalid Zodiac sign")

def get_october_fortune(zodiac):
    october_fortunes = {
        "Rat": "This month, Rats should focus on seizing opportunities that come their way. Stay adaptable and trust your instincts. Your intelligence will guide you to success.",
        "Ox": "Hard work pays off for Oxen this month. Remember to balance work with self-care. Your diligence and dependability will be rewarded.",
        "Tiger": "Embrace your adventurous spirit, Tigers. This month, pursue your dreams with confidence. Your courage will lead to exciting new experiences.",
        "Rabbit": "Diplomacy and gentleness are key for Rabbits in October. Navigating relationships will lead to success. Trust your instincts in social situations.",
        "Dragon": "Tap into your inner strength and ambition, Dragons. This month, pursue your goals with determination. You have the power to achieve great things.",
        "Snake": "Trust your wisdom and intuition, Snakes. Be open to transformation. Embrace change, and you'll find new opportunities for growth.",
        "Horse": "Independence and energy define the month for Horses. Explore new horizons and seize the day. Your vitality will lead to exciting adventures.",
        "Goat": "Let creativity and kindness flourish, Goats. Spread positivity and imagination. Your optimism will inspire those around you.",
        "Monkey": "Adaptability and wit are your strengths, Monkeys. Embrace change and use your intelligence to overcome challenges. You have the tools to succeed.",
        "Rooster": "Confidence and honesty define your month, Roosters. Stand tall and be true to yourself. Your authenticity will lead to positive outcomes.",
        "Dog": "Loyalty and reliability are your pillars, Dogs. Your steadfastness will be a source of strength. Support those around you, and you'll find fulfillment.",
        "Pig": "Generosity and optimism shine this month, Pigs. Focus on building meaningful connections. Enjoy the abundance life has to offer."
    }
    return october_fortunes.get(zodiac, "Invalid Zodiac sign")

def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        print("Welcome to the Chinese Zodiac Game!")
        birth_year = int(input("What year were you born? "))
        
        if 1960 <= birth_year <= 2023:
            zodiac = determine_zodiac(birth_year)
            print(f"You were born in the year of the {zodiac}.")
            
            fortune_question = input("Do you want to know your fortune this year? (Yes/No) ").lower()
            if fortune_question == "yes":
                fortune = get_fortune(zodiac)
                print(fortune)
                
                october_fortune_question = input("Are you willing to see the current fortune in October 2023? (Yes/No) ").lower()
                if october_fortune_question == "yes":
                    october_fortune = get_october_fortune(zodiac)
                    print(october_fortune)
                else:
                    print("Goodbye! Have a nice day.")
            else:
                print("Goodbye! Have a nice day.")
        else:
            print("Invalid input. Please enter a valid birth year between 1900 and 2023.")
        
        play_again = input("Do you want to play again? (Yes/No) ")
    
    print("This game is for entertainment purposes only. Trust yourself!")

if __name__ == "__main__":
    main()
