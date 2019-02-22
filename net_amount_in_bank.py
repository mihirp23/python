## Mihir Patel
## 2/22/19
## A program that computes the net amount of bank account
## based on a transaction log from console input.
## The transaction log format should be as follows:
## D 100
## W 200
## Where D means 'Deposit' and 'W' means withdrawal.
## File : net_amount_in_bank.py

############################################################
def main():
############################################################

    # initialize bank amounts
    net_amount = 0
    total_withdrawal = 0
    total_deposit = 0

    # prompt user for bank transaction log
    while (True):
        inp_str = input()
        if not inp_str:
            break

        inp_list = inp_str.split(" ")
        operation = inp_list[0]

        if operation == 'D':
            net_amount += int(inp_list[1])
            total_deposit += int(inp_list[1])
        elif operation == 'W':
            net_amount -= int(inp_list[1])
            total_withdrawal = int(inp_list[1])
        else:
            continue

    # print a breakdown of account transactions
    print("             Net Amount : " + str(net_amount))
    print("   Total Deposit Amount : " + str(total_deposit))
    print("Total Withdrawal Amount : " + str(total_withdrawal))

# main()
    

if __name__ == "__main__":
    main()
