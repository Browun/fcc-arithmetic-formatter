from operator import add, sub
from typing import List, Optional

def arithmetic_arranger(problems: List[str], show_answer: Optional[bool] = False):
    '''
    Checks the arithmetic inputs (problems) and produces their long hand form.
    '''

    # Check the input meets the criteria
    check_output = check_inputs(problems)

    if isinstance(check_output, str):
        return check_output

    # Process the inputs
    arranged_problems = arrange_inputs(problems, show_answer)

    return arranged_problems


def check_inputs(problems: List[str]):
    '''
    Checks the provided problems are:
    - Of length 1-5 inclusively
    - Only contains addition and subtraction operators
    - Only contains integers
    - Only contains integers up to 4 digits in length

    Returns True if all of the above conditions are met, otherwise returns a string error message.
    '''

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        operand_one, operator, operand_two = problem.split(" ")

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if len(operand_one) > 4 or len(operand_two) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if not (operand_one + operand_two).isdigit():
            return "Error: Numbers must only contain digits."

    return True


def arrange_inputs(problems: List[str], show_answer: bool):
    '''
    Renders each input provided vertically, with the relevant operator, and optional answer if show_answer is True.
    '''

    # Instantiate variables
    line_one, line_two, line_three, line_four = '', '', '', ''
    gap: str = '    '

    for problem in problems:
        # Assign the variables for the problem
        operand_one, operator, operand_two = problem.split(" ")
        operator_function = add if operator == '+' else sub
        # Find the width from max operand length
        assignment_width: int = max(len(operand_one), len(operand_two)) + 2

        line_one += operand_one.lstrip().rjust(assignment_width) + gap
        line_two += operator + operand_two.rjust(assignment_width - 1) + gap
        line_three += "-" * assignment_width + gap

        if show_answer == True:

            line_four += str(operator_function(int(operand_one), int(operand_two))).rjust(assignment_width) + gap
    
    # Conditionally add a line seperator if show_answer is true
    final_lines = line_three.rstrip() + '\n' + line_four.rstrip() if show_answer == True else line_three.rstrip()

    output: str = line_one.rstrip() + '\n' + line_two.rstrip() + '\n' + final_lines

    return output
