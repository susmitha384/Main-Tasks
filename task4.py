# Smart To-Do & Habit Companion 
# A console-based app using only core Python. 
# Features: Add/view/mark tasks, track habits with streaks, daily wellness insight. 
def main(): 

    tasks = []  # List of tasks: [{'desc': str, 'done': bool}] 
    habits = []  # List of habits: [{'desc': str, 'streak': int, 'done_today': bool}] 

    while True: 

        print("\n=== Smart To-Do & Habit Companion ===") 

        print("1. Add Task") 

        print("2. View Tasks") 

        print("3. Mark Task as Done") 

        print("4. Add Habit") 

        print("5. View Habits") 

        print("6. Mark Habit as Done") 

        print("7. Get Daily Wellness Insight") 

        print("8. Exit") 

        choice = input("Choose an option (1-8): ").strip() 

        if choice == '1': 
            desc = input("Enter task description: ").strip() 

            if desc: 
                tasks.append({'desc': desc, 'done': False}) 
                print("Task added!") 
            else: 

                print("Description cannot be empty.") 
        elif choice == '2': 
            if not tasks: 
                print("No tasks yet.") 

            else: 
                for i, task in enumerate(tasks, 1): 
                    status = "Done" if task['done'] else "Pending" 

                    print(f"{i}. {task['desc']} - {status}") 
        elif choice == '3': 

            if not tasks: 
                print("No tasks to mark.") 

            else: 
                view_tasks(tasks) 

                try: 
                    idx = int(input("Enter task number to mark as done: ")) - 1 

                    if 0 <= idx < len(tasks): 
                        tasks[idx]['done'] = True 
                        print("Task marked as done!") 

                    else: 

                        print("Invalid number.") 

                except ValueError: 

                    print("Please enter a valid number.") 
        elif choice == '4': 

            desc = input("Enter habit description: ").strip() 
            if desc: 
                habits.append({'desc': desc, 'streak': 0, 'done_today': False}) 

                print("Habit added!") 
            else: 
                print("Description cannot be empty.") 

        elif choice == '5': 
            if not habits: 

                print("No habits yet.") 
            else: 
                for i, habit in enumerate(habits, 1): 
                    status = "Done today" if habit['done_today'] else "Not done today" 

                    print(f"{i}. {habit['desc']} - Streak: {habit['streak']} days - {status}") 
        elif choice == '6': 
            if not habits: 

                print("No habits to mark.") 
            else: 

                view_habits(habits) 
                try: 

                    idx = int(input("Enter habit number to mark as done today: ")) - 1 
                    if 0 <= idx < len(habits): 

                        if not habits[idx]['done_today']: 

                            habits[idx]['streak'] += 1 

                            habits[idx]['done_today'] = True 

                            print("Habit marked as done! Streak increased.") 

                        else: 

                            print("Habit already marked as done today.") 

                    else: 

                        print("Invalid number.") 

                except ValueError: 

                    print("Please enter a valid number.") 
        elif choice == '7': 

            # Calculate wellness insight 

            if not tasks and not habits: 

                print("Add some tasks and habits first for an insight!") 

            else: 
                task_completion = sum(1 for t in tasks if t['done']) / len(tasks) * 100 if tasks else 0 

                avg_streak = sum(h['streak'] for h in habits) / len(habits) if habits else 0 

                insight = generate_insight(task_completion, avg_streak) 

                print(f"\nDaily Wellness Insight:\n{insight}") 
        elif choice == '8': 

            print("Goodbye!") 
            break 
        else: 

            print("Invalid choice. Try again.") 
def view_tasks(tasks): 

    print("Current Tasks:") 

    for i, task in enumerate(tasks, 1): 
        status = "Done" if task['done'] else "Pending" 
        print(f"{i}. {task['desc']} - {status}") 

def view_habits(habits): 

    print("Current Habits:") 
    for i, habit in enumerate(habits, 1): 

        status = "Done today" if habit['done_today'] else "Not done today" 

        print(f"{i}. {habit['desc']} - Streak: {habit['streak']} days - {status}") 

def generate_insight(task_pct, avg_streak): 
    if task_pct >= 80 and avg_streak >= 7: 

        return "Excellent! You're crushing your goals with high task completion and strong habit streaks. Keep it up!" 

    elif task_pct >= 60 and avg_streak >= 3: 

        return "Good job! You're making progress on tasks and building habits. A little more consistency will take you far." 

    elif task_pct >= 40 or avg_streak >= 1: 

        return "Not bad, but there's room for improvement. Focus on completing more tasks and maintaining those habits." 

    else: 
        return "Let's get started! Add some tasks and habits, and aim to complete them daily for better wellness." 
if __name__ == "__main__": 

    main() 