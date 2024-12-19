def calculate_love_score(name_1, name_2):
    true = "TRUE"
    love = "LOVE"

    def count_true_love(person_one, person_two, what):
        count = 0

        name = ""
        for i in person_one:
            name += i

        for j in person_two:
            name += j

        combined_name = name.upper()
        # print(new_name)

        for i in combined_name:
            for j in what:
                if i == j:
                    count += 1
        return count

    true_count = count_true_love(name_1, name_2, true)
    love_count = count_true_love(name_1, name_2, love)

    print(f"{true_count}{love_count}")


calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")