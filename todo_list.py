{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d388975-9268-4760-8ae3-81bfa33c80ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "tasks = []\n",
    "\n",
    "def show_tasks():\n",
    "    if not tasks:\n",
    "        print(\"\\nNo tasks available.\")\n",
    "    else: \n",
    "        print(\"\\nYour To-Do List:\")\n",
    "        for i, task in enumerate(tasks,1):\n",
    "            print(f\"{i}.{task}\")\n",
    "\n",
    "def add_task():\n",
    "    task = input(\"Enter a new task:\")\n",
    "    tasks.append(task)\n",
    "    print(\"Task added successfully!.\")\n",
    "\n",
    "def remove_task():\n",
    "    show_tasks()\n",
    "    try:\n",
    "        task_no = int(input(\"Enter the task number to remove:\")) - 1\n",
    "        if 0 <= task_no < len(tasks):\n",
    "            removed = tasks.pop(task_no)\n",
    "            print(f\"Task '{removed}' removed successfully!\")\n",
    "        else:\n",
    "            print(\"Invalid task number.\")\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"Please enter a valid number.\")\n",
    "\n",
    "while True:\n",
    "    print(\"\\n1. Show Tasks\\n2. Add Tasks\\n3. Remove Task\\n4. Exit\")\n",
    "    choice = input(\"choose an option:\")\n",
    "\n",
    "    if choice == \"1\":\n",
    "        show_tasks()\n",
    "\n",
    "    elif choice == \"2\":\n",
    "        add_task()\n",
    "\n",
    "    elif choice == \"3\":\n",
    "        remove_task()\n",
    "\n",
    "    elif choice == \"4\":\n",
    "        print(\"Goodbye\")\n",
    "        break\n",
    "    else:\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
