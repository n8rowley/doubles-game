## Requirements

- Display game setup menu
    - display welcome message
    - get info
        - number of rounds
        - players
        - (if a special key is pressed, provide random range options)

- Show round status
    - Info
        - Round #
        - Round total
        - 7's counter
    - Features 
        - visual que for third 7

- Show current standings
    - Info
        - player's name
        - player's score
        - distance from the leader
    - Features
        - display with highest score on top
        - display players in a stable order for tied scores

- Provide an input line
    - Handled Data
        - Normal roll result(3-11, exluding 7's and doubles)
            - add result to round total
        - 7
            - add 75 to the round total
            - increase 7's counter
        - Doubles
            - double current score
            - (if total is 0, get the # rolled)
        - Special roll key (something on the keypad)
            - peform special function
        - edit flag
            - display all editable fields and their flag
            - provide an error flag input line