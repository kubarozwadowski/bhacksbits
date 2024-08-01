class Domino:
    def __init__(self, left: str, operation: str, right: str):
        self.left = left  
        self.operation = operation  
        self.right = right 

    def flip(self):
        #Swaps left and right numbers, inverts operation
        self.operation = 'OR' if self.operation == 'AND' else 'AND'
        self.left, self.right = self.right, self.left

    def evaluate(self):
        #Evaluates value of domnio
        left_int = int(self.left, 2)
        right_int = int(self.right, 2)
        if self.operation == 'AND':
            return format(left_int & right_int, '04b')
        else:
            return format(left_int | right_int, '04b')

    def __str__(self):
        return f"[{self.left} {self.operation} {self.right}]"

class BinaryGame:
    def __init__(self, dominos, separating_operations, desired_output):
        self.dominos = dominos  
        self.separating_operations = separating_operations  
        self.desired_output = desired_output  

    def flip_domino(self, index):
        if 0 <= index < len(self.dominos):
            self.dominos[index].flip()
        else:
            print("Invalid index.")

    def flip_separating_operation(self, index):
        """Flip the separating operation at the specified index."""
        if 0 <= index < len(self.separating_operations):
            self.separating_operations[index] = 'OR' if self.separating_operations[index] == 'AND' else 'AND'
        else:
            print("Invalid index.")

    def evaluate(self):
        """Evaluate the combined result of the three dominos with the separating operations."""
        result1 = self.dominos[0].evaluate()
        result2 = self.dominos[1].evaluate()
        result3 = self.dominos[2].evaluate()

        intermediate_result1 = (int(result1, 2) & int(result2, 2)) if self.separating_operations[0] == 'AND' else (int(result1, 2) | int(result2, 2))
        final_result = (intermediate_result1 & int(result3, 2)) if self.separating_operations[1] == 'AND' else (intermediate_result1 | int(result3, 2))

        return format(final_result, '04b')

    def is_solved(self):
        """Check if the current configuration matches the desired output."""
        return self.evaluate() == self.desired_output

    def __str__(self):
        return f"{self.dominos[0]} {self.separating_operations[0]} {self.dominos[1]} {self.separating_operations[1]} {self.dominos[2]}\nDesired Output: {self.desired_output}"

def main():
    dominos = [
        Domino('1010', 'OR', '1101'),
        Domino('0110', 'AND', '0011'),
        Domino('0111', 'AND', '0110')
    ]
    separating_operations = ['AND', 'OR']
    desired_output = '0100'
    game = BinaryGame(dominos, separating_operations, desired_output)

    while not game.is_solved():
        print(game)
        action = input("Enter 'd' to flip a domino or 's' to flip a separating operation: ")
        if action == 'd':
            try:
                index = int(input("Enter the index of the domino to flip (0, 1, or 2): "))
                game.flip_domino(index)
                print("\nUpdated Game State:")
                print(game)
            except ValueError:
                print("Please enter a valid integer index.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif action == 's':
            try:
                index = int(input("Enter the index of the separating operation to flip (0 or 1): "))
                game.flip_separating_operation(index)
                print("\nUpdated Game State:")
                print(game)
            except ValueError:
                print("Please enter a valid integer index.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid action. Please enter 'd' or 's'.")
    
    print("Congratulations! You've solved the game!")

if __name__ == "__main__":
    main()
