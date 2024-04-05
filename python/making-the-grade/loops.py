"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    
    rounded_scores = []

    for score in student_scores:
        rounded_scores.append(round(score))
    
    return rounded_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failed_count = 0
    for score in student_scores:
        if score <= 40:
            failed_count += 1
    return failed_count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    
    top_scores = []
    for student_score in student_scores:
        if student_score >= threshold:
            top_scores.append(student_score)
    
    return top_scores

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    failing_grade = 40  # Implicit assumption, might need adjustment
    num_grades = 4  # Number of letter grades (A, B, C, D)

    interval_size = (highest - failing_grade + 1) // num_grades

    thresholds = [failing_grade + 1 + idx * interval_size for idx in range(num_grades)]

    return thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranked_scores = []
    for index, name in enumerate(student_names):
        rank = index + 1
        ranked_scores.append(f'{rank}. {name}: {student_scores[index]}')

    return ranked_scores
        


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    perfect_student = []
    for name, score in student_info:
        if score == 100:
            perfect_student.append(name)
            perfect_student.append(score)
            break

    return perfect_student
