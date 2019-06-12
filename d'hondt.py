total_seats = int(input("Number of seats: "))
MIN_PERCENTAGE = int(input("Minimum percentage: "))
raw_parties = []
raw_votes  = []

while True:
    inputs = str(input("")).split(" ")
    if inputs[0] == "exit":
        break
    elif len(inputs) == 2:
        party = inputs[0]
        num_votes = int(inputs[1])
        raw_parties.append(party)
        raw_votes.append(num_votes)
    else:
        print("Not recognized")

parties = []
votes = []
division = []
seats = []

for x in range(len(raw_votes)):
    if raw_votes[x] / sum(raw_votes) * 100 >= MIN_PERCENTAGE:
        parties.append(raw_parties[x])
        votes.append(raw_votes[x])
        division.append(1)
        seats.append(0)

for x in range(total_seats):
    biggest_party = parties[0]
    party_sum = votes[0] / division[0]
    for y in range(len(parties)):
        if votes[y] / division[y] > party_sum:
            biggest_party = parties[y]
            party_sum = votes[y] / division[y]
    division[parties.index(biggest_party)] += 1
    seats[parties.index(biggest_party)] += 1

for x in range(len(parties)):
    print(parties[x], seats[x])
