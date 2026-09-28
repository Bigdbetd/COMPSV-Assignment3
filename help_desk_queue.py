from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        return None if self.front is None else self.front.value

    def print_queue(self):
        current = self.front
        while current is not None:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")
        elif choice == "2":
            name = queue.dequeue()
            print("No customers waiting" if name is None else f"Helped: {name}")
        elif choice == "3":
            name = queue.peek()
            print("No customers waiting" if name is None else f"Next customer: {name}")
        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()
        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
