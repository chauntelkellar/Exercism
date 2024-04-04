"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

from statistics import mean

def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    current_round = round(number)
    next_rounds = [round(number + idx) for idx in range(1,3)]
    return [current_round] + next_rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2 


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds 

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return mean(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # Calculate the true average of the hand
    true_average = sum(hand) / len(hand)

    # Check for approximate averages
    approx_average1 = (hand[0] + hand[-1]) / 2  # Average of first and last card
    approx_average2 = hand[len(hand) // 2] if len(hand) % 2 == 1 else None  # Middle card (if odd number of cards)

    # Return True if either approximate average matches the true average
    return true_average in (approx_average1, approx_average2)

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    if len(hand) <= 1:
        return False  # Handle empty or single-card hands

    # Separate even and odd indexed elements using list comprehension
    even_elements = [hand[idx] for idx in range(0, len(hand), 2)]
    odd_elements = [hand[idx] for idx in range(1, len(hand), 2)]

    # Calculate averages using sum and division
    even_average = sum(even_elements) / len(even_elements)
    odd_average = sum(odd_elements) / len(odd_elements)

    # Return True if even and odd averages are equal
    return even_average == odd_average


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if not hand or hand[-1] != 11:  # Check for empty hand or non-Jack at last index
        return hand

    # Create a copy to avoid modifying the original hand
    doubled_hand = hand.copy()
    doubled_hand[-1] *= 2  # Double the value of the last element (Jack)

    return doubled_hand
