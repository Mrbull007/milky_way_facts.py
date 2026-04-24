import random

# List of interesting facts about the Milky Way (sourced from NASA, Space.com, Wikipedia, etc.)
facts = [
    "The Milky Way is a barred spiral galaxy approximately 100,000 light-years across and about 1,000 light-years thick at the spiral arms.",
    "It contains an estimated 100–400 billion stars and at least that many planets.",
    "At the center lies Sagittarius A*, a supermassive black hole with a mass of about 4 million times that of our Sun.",
    "Our Solar System is located about 27,000 light-years from the galactic center, on the inner edge of the Orion Arm.",
    "It takes the Solar System roughly 225–250 million years to complete one orbit around the Milky Way's center (a 'galactic year').",
    "The Milky Way is about 13.6 billion years old — almost as old as the universe itself.",
    "Around 90% of the galaxy's mass is invisible dark matter, forming a large halo around the visible disk.",
    "From Earth, the Milky Way appears as a faint, milky band of light across the night sky, which gave it its name (from Latin 'via lactea').",
    "The galaxy is warped like a vinyl record due to gravitational interactions with satellite galaxies.",
    "It is part of the Local Group, which includes over 50 other galaxies, and will collide with the Andromeda Galaxy in about 4–5 billion years.",
    "The oldest known star in the Milky Way is HD 140283 (Methuselah star), estimated at 13.6 billion years old.",
    "The Milky Way is still growing by 'eating' smaller galaxies, such as the Magellanic Clouds.",
    "If the Milky Way were scaled to 100 meters wide, our Solar System would be about 1 millimeter across.",
    "The galaxy is moving through space at around 600 km/s (373 miles per second).",
    "There may be around 100 million stellar-mass black holes roaming the galaxy."
]

def display_menu():
    print("\n" + "="*60)
    print("🌌 INTERACTIVE RANDOM MILKY WAY FACTS 🌌")
    print("="*60)
    print("1. Get a Random Fact")
    print("2. Show All Facts")
    print("3. Quit")
    print("="*60)

def main():
    print("Welcome to the Milky Way Galaxy Fact Explorer!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            fact = random.choice(facts)
            print("\n🌟 RANDOM FACT:")
            print(fact)
            print("-" * 60)
        elif choice == "2":
            print("\n📋 ALL MILKY WAY FACTS:")
            for i, fact in enumerate(facts, 1):
                print(f"{i}. {fact}")
            print("-" * 60)
        elif choice == "3":
            print("Thanks for exploring the galaxy! Keep looking up. 🌠")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
