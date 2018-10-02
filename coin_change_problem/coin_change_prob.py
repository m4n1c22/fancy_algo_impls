#Coin change problem using greedy approach

coin_changes = [1,2,5,10,20,50,100]
changes = {}

def optimum_least(amt_left):
    if coin_changes[0] > amt_left:
        return -1
    for i in range(len(coin_changes)-1):
        if (coin_changes[i]<=amt_left) and (coin_changes[i+1]>amt_left):
            return i
    if coin_changes[i]<amt_left:
        return i

def calculate_coin_change(change_amt):
    amt_left = change_amt
    while amt_left != 0:
        idx = optimum_least(amt_left)
        amt_left = amt_left - coin_changes[idx]
        if coin_changes[idx] not in changes:
            changes[coin_changes[idx]] = 0
        changes[coin_changes[idx]] += 1;
    print (changes)

def main():
    change_amt = input("\nEnter change amount required: ")
    calculate_coin_change(change_amt)

if __name__ == '__main__':
    main()
