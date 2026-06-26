from tasks import (
    create_task,
    delete_task,
    get_all_stats,
    show_tasks,
    show_urgent_tasks,
    update_task_completion,
)

from storage import save_tasks, load_tasks

def show_menu():
    print("\n       Меню\n")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Показать статусы задач")
    print("4. Показать срочные задачи")
    print("5. Изменить процент выполнения")
    print("6. Удалить задачу")
    print("0. Выход")




def main():
    tasks = load_tasks()
    
    while True:
        show_menu()

        command = int(input("\nВведите номер команды: "))

        if command == 1:
            task = create_task()

            if task is not None:
                tasks.append(task)
                save_tasks(tasks)
                
                print("Задача успешно добавлена")
        elif command == 2:
            show_tasks(tasks)
        
        elif command == 3:
            get_all_stats(tasks)

        elif command == 4:
            show_urgent_tasks(tasks)

        elif command == 5:
            update_task_completion(tasks)
            save_tasks(tasks)

        elif command == 6:
            delete_task(tasks)
            save_tasks(tasks)

        elif command == 0:
            print("Программа завершена")
            break
        
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()