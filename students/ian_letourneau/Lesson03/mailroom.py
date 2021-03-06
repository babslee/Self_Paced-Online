#!/usr/bin/env python3
# Ian Letourneau
# 5/2/2018
# A script that stores values for donors and their donations.
# The script can process requests from the user on various functions
# to utilize these values

# Build a dictionary of existing donors
donors = {
    "Bill Gates": [1235544.00, 456789.50, 2347899.75],
    "Jimmy Kimmel": [456.37, 25.67, 999876.00, 2134.78, 3.14],
    "LeBron James": [6578921.00, 3.50, 23400.00, 7234.00]
}


def send_thank_you():
    """A function that takes in no parameters, This function allows the user
    to lookup a list of existing donors as well as add a new donor to the
    list. Once a name is chosen, the function prompts the user for an amount
    donated and will add the donation to that donor's donations in the
    dictionary. Finally, the script prints a thank you letter to that donor.
    To quit to the main menu, 'q' can be typed at any user prompt."""
    print("")
    namePrompt = ("Please enter a full name to send to or enter"
                  " 'list' for a full list of donors('q' to quit to menu): ")
    name = input(namePrompt)
    if name == 'q':
        return ("Heading back to the main menu.")

    # If list is chosen, print a list of donors and reprompt for a name, 'q'
    # to quit to main menu
    while name == 'list':
        for donor in donors:
            print(donor)
        name = input(namePromt)
        if name == 'q':
            return ("Heading back to the main menu.")
    # Once name is input, prompt for a donation amount, 'q' to quit
    amount = input(
        "Please enter the amount that was donated('q' to quit to menu): ")
    if amount == 'q':
        return ("Heading back to the main menu.")

    # Once amount is input, add the donation to the donor key if existing
    # or add both the donor and the donation to the dictionary if new
    amount = float(amount)
    if name in donors.keys():
        donors[name].append(amount)
    else:
        donors.setdefault(name, [])
        donors[name].append(amount)

    print('Dear {}, we wanted to say thank you for your generous'
          ' donation of ${}!'.format(name, amount))


def create_report():
    """A function that takes no paramters. This function creates a report
    from existing donors and their donations to output donor name,
    total amount donated, number of donations, and average donation amount."""
    # Find longest name to adjust size of table
    name_length = 0
    running_total = 0
    total_dict = {}
    sorted_dict = {}
    sorted_list = []

    # Loop through donors and track longest name and total donations.
    # Sort donors by total donations
    for name in donors.keys():
        total = 0
        if len(name) > name_length:
            name_length = len(name)
        donations = donors[name]
        for value in donations:
            total += value
            total_dict[name] = total
    sorted_list = sorted(total_dict.values(), reverse=True)
    for sorted_key in sorted_list:
        for key, value in total_dict.items():
            if value == sorted_key:
                sorted_dict[key] = value

    # Print header line of table adjusting column length by length of name
    print("")
    print("{:{align}{width}} | {:<10} | {:<10} | {:<10}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift",
        align='<', width=str(name_length+1)))
    print("-"*(name_length+43))

    # Loop through each donor and print their entry based on data in dictionary
    for name in sorted_dict:
        donations = donors[name]
        don_length = (len(donations))
        average = (sorted_dict[name]/don_length)

        print("{:{align}{width}} $ {:>11.2f}   {:>10d} $ {:>10.2f}".format(
            name, sorted_dict[name], don_length, average,
            align='<', width=str(name_length+2)))


if __name__ == '__main__':
    """This area is always exectued by the script. It contains the main
    menu prompt as well as the calls to the previous two functions
    depending on which option was chosen. The third option allows
    the user to quit the script."""
    response = ''
    # Prompt menu and repeat until the "Quit" option has been chosen
    while response != 3:
        print("""\nHello User! What would you like to do?
1) Send a Thank You card
2) Create a report of donors
3) Quit \n""")
        response = int(
            input("Please input a numerical value for"
                  " what you would like to do: "))
        while response not in (1, 2, 3,):
            response = int(
                input("Invalid answer. Please input a numerical"
                      " value for what you would like to do: "))
        # Once response has been verified and is not 3 to quit,
        # call the appropriate function
        if response == 1:
            send_thank_you()
        elif response == 2:
            create_report()
