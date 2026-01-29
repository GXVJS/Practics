import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.title("Игнатушин Павел Николаевич ЗИТ-252")
        self.geometry("800x600")
        self.configure(bg='#f0f0f0')

        # Создаем Notebook (вкладки)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Создаем вкладки
        self.create_calculator_tab()
        self.create_checkboxes_tab()
        self.create_text_editor_tab()

        # Создаем строку статуса
        self.status_var = tk.StringVar()
        self.status_var.set("Готово")
        self.status_bar = tk.Label(self, textvariable=self.status_var,
                                   bd=1, relief=tk.SUNKEN, anchor=tk.W,
                                   bg='#e0e0e0', fg='#333333')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_calculator_tab(self):
        """Создание вкладки калькулятора"""
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text='Калькулятор')

        # Заголовок
        title_label = tk.Label(calc_frame, text="Калькулятор",
                               font=('Arial', 16, 'bold'),
                               bg='#f0f0f0')
        title_label.pack(pady=20)

        # Фрейм для ввода чисел
        input_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        input_frame.pack(pady=20)

        # Первое число
        num1_frame = tk.Frame(input_frame, bg='#f0f0f0')
        num1_frame.pack(side=tk.LEFT, padx=10)

        num1_label = tk.Label(num1_frame, text="Первое число:",
                              bg='#f0f0f0', font=('Arial', 11))
        num1_label.pack(anchor='w')

        self.num1_var = tk.StringVar()
        num1_entry = tk.Entry(num1_frame, textvariable=self.num1_var,
                              font=('Arial', 11), width=15,
                              relief=tk.SOLID, bd=2)
        num1_entry.pack(pady=5)

        # Операция
        operation_frame = tk.Frame(input_frame, bg='#f0f0f0')
        operation_frame.pack(side=tk.LEFT, padx=10)

        operation_label = tk.Label(operation_frame, text="Операция:",
                                   bg='#f0f0f0', font=('Arial', 11))
        operation_label.pack(anchor='w')

        self.operation_var = tk.StringVar(value="+")
        operation_combo = ttk.Combobox(operation_frame,
                                       textvariable=self.operation_var,
                                       values=["+", "-", "*", "/"],
                                       state='readonly', width=5,
                                       font=('Arial', 11))
        operation_combo.pack(pady=5)

        # Второе число
        num2_frame = tk.Frame(input_frame, bg='#f0f0f0')
        num2_frame.pack(side=tk.LEFT, padx=10)

        num2_label = tk.Label(num2_frame, text="Второе число:",
                              bg='#f0f0f0', font=('Arial', 11))
        num2_label.pack(anchor='w')

        self.num2_var = tk.StringVar()
        num2_entry = tk.Entry(num2_frame, textvariable=self.num2_var,
                              font=('Arial', 11), width=15,
                              relief=tk.SOLID, bd=2)
        num2_entry.pack(pady=5)

        # Кнопка вычисления
        calc_button = tk.Button(calc_frame, text="Вычислить",
                                command=self.calculate_tk,
                                font=('Arial', 11, 'bold'),
                                bg='#4CAF50', fg='white',
                                relief=tk.RAISED, bd=2,
                                padx=20, pady=10)
        calc_button.pack(pady=20)

        # Результат
        result_frame = tk.Frame(calc_frame, bg='#f0f0f0')
        result_frame.pack(pady=10)

        result_label = tk.Label(result_frame, text="Результат:",
                                bg='#f0f0f0', font=('Arial', 11))
        result_label.pack(anchor='w')

        self.result_var = tk.StringVar()
        result_entry = tk.Entry(result_frame, textvariable=self.result_var,
                                font=('Arial', 11), width=30,
                                relief=tk.SOLID, bd=2, state='readonly',
                                bg='#f9f9f9')
        result_entry.pack(pady=5)

    def create_checkboxes_tab(self):
        """Создание вкладки с чекбоксами"""
        check_frame = ttk.Frame(self.notebook)
        self.notebook.add(check_frame, text='Чекбоксы')

        # Заголовок
        title_label = tk.Label(check_frame, text="Выбор вариантов",
                               font=('Arial', 16, 'bold'),
                               bg='#f0f0f0')
        title_label.pack(pady=20)

        # Инструкция
        instruction_label = tk.Label(check_frame,
                                     text="Выберите один или несколько вариантов:",
                                     font=('Arial', 11),
                                     bg='#f0f0f0')
        instruction_label.pack(pady=10)

        # Чекбоксы
        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        self.check_var3 = tk.BooleanVar()

        checkbox1 = tk.Checkbutton(check_frame, text="Первый вариант",
                                   variable=self.check_var1,
                                   font=('Arial', 11),
                                   bg='#f0f0f0')
        checkbox1.pack(pady=5)

        checkbox2 = tk.Checkbutton(check_frame, text="Второй вариант",
                                   variable=self.check_var2,
                                   font=('Arial', 11),
                                   bg='#f0f0f0')
        checkbox2.pack(pady=5)

        checkbox3 = tk.Checkbutton(check_frame, text="Третий вариант",
                                   variable=self.check_var3,
                                   font=('Arial', 11),
                                   bg='#f0f0f0')
        checkbox3.pack(pady=5)

        # Кнопка подтверждения
        select_button = tk.Button(check_frame, text="Подтвердить выбор",
                                  command=self.show_selection_tk,
                                  font=('Arial', 11, 'bold'),
                                  bg='#2196F3', fg='white',
                                  relief=tk.RAISED, bd=2,
                                  padx=20, pady=10)
        select_button.pack(pady=20)

        # Область для отображения выбора
        self.selection_text = tk.Text(check_frame, height=5, width=50,
                                      font=('Arial', 10),
                                      relief=tk.SOLID, bd=2)
        self.selection_text.pack(pady=10, padx=20)
        self.selection_text.insert('1.0', "Здесь будет отображен ваш выбор...")
        self.selection_text.config(state='disabled')

    def create_text_editor_tab(self):
        """Создание вкладки текстового редактора"""
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text='Текстовый редактор')

        # Заголовок
        title_label = tk.Label(text_frame, text="Текстовый редактор",
                               font=('Arial', 16, 'bold'),
                               bg='#f0f0f0')
        title_label.pack(pady=10)

        # Панель инструментов
        toolbar = tk.Frame(text_frame, bg='#f0f0f0')
        toolbar.pack(fill=tk.X, padx=10, pady=10)

        # Кнопки
        load_button = tk.Button(toolbar, text="Загрузить файл",
                                command=self.load_file_tk,
                                font=('Arial', 10),
                                bg='#FF9800', fg='white',
                                relief=tk.RAISED, bd=2)
        load_button.pack(side=tk.LEFT, padx=5)

        save_button = tk.Button(toolbar, text="Сохранить файл",
                                command=self.save_file_tk,
                                font=('Arial', 10),
                                bg='#4CAF50', fg='white',
                                relief=tk.RAISED, bd=2)
        save_button.pack(side=tk.LEFT, padx=5)

        clear_button = tk.Button(toolbar, text="Очистить",
                                 command=self.clear_text_tk,
                                 font=('Arial', 10),
                                 bg='#f44336', fg='white',
                                 relief=tk.RAISED, bd=2)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Текстовое поле
        self.text_widget = tk.Text(text_frame, font=('Arial', 11),
                                   relief=tk.SOLID, bd=2,
                                   wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Добавляем прокрутку
        scrollbar = tk.Scrollbar(self.text_widget)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_widget.yview)

        # Статистика
        stats_frame = tk.Frame(text_frame, bg='#f0f0f0')
        stats_frame.pack(fill=tk.X, padx=10, pady=5)

        self.char_count_var = tk.StringVar(value="Символов: 0")
        self.word_count_var = tk.StringVar(value="Слов: 0")

        char_label = tk.Label(stats_frame, textvariable=self.char_count_var,
                              bg='#f0f0f0', font=('Arial', 10))
        char_label.pack(side=tk.LEFT, padx=10)

        word_label = tk.Label(stats_frame, textvariable=self.word_count_var,
                              bg='#f0f0f0', font=('Arial', 10))
        word_label.pack(side=tk.LEFT, padx=10)

        # Привязываем обновление статистики к изменению текста
        self.text_widget.bind('<KeyRelease>', self.update_counts_tk)

    def calculate_tk(self):
        """Выполнение вычислений (tkinter версия)"""
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = num1 / num2

            self.result_var.set(str(result))
            self.status_var.set(f"Результат: {result}")

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")
            self.status_var.set("Ошибка: некорректный ввод")
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
            self.status_var.set("Ошибка: деление на ноль")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
            self.status_var.set(f"Ошибка: {str(e)}")

    def show_selection_tk(self):
        """Отображение выбранных вариантов (tkinter версия)"""
        selected = []

        if self.check_var1.get():
            selected.append("Первый")
        if self.check_var2.get():
            selected.append("Второй")
        if self.check_var3.get():
            selected.append("Третий")

        if selected:
            message = f"Вы выбрали: {', '.join(selected)} вариант(ы)"
            messagebox.showinfo("Ваш выбор", message)

            # Отображаем в текстовом поле
            self.selection_text.config(state='normal')
            self.selection_text.delete('1.0', tk.END)
            self.selection_text.insert('1.0', message)
            self.selection_text.config(state='disabled')

            self.status_var.set(message)
        else:
            messagebox.showwarning("Внимание", "Вы не выбрали ни одного варианта!")
            self.status_var.set("Не выбрано ни одного варианта")

    def load_file_tk(self):
        """Загрузка файла (tkinter версия)"""
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert('1.0', content)

                # Переключаемся на вкладку редактора
                self.notebook.select(2)

                filename = os.path.basename(file_path)
                self.status_var.set(f"Файл загружен: {filename}")
                messagebox.showinfo("Успех", f"Файл '{filename}' загружен!")

                self.update_counts_tk()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {str(e)}")
                self.status_var.set(f"Ошибка загрузки: {str(e)}")

    def save_file_tk(self):
        """Сохранение файла (tkinter версия)"""
        file_path = filedialog.asksaveasfilename(
            title="Сохранить файл",
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        if file_path:
            try:
                content = self.text_widget.get('1.0', tk.END)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)

                filename = os.path.basename(file_path)
                self.status_var.set(f"Файл сохранен: {filename}")
                messagebox.showinfo("Успех", f"Файл '{filename}' сохранен!")

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
                self.status_var.set(f"Ошибка сохранения: {str(e)}")

    def clear_text_tk(self):
        """Очистка текста (tkinter версия)"""
        if messagebox.askyesno("Подтверждение", "Очистить текст?"):
            self.text_widget.delete('1.0', tk.END)
            self.status_var.set("Текст очищен")
            self.update_counts_tk()

    def update_counts_tk(self, event=None):
        """Обновление счетчиков (tkinter версия)"""
        text = self.text_widget.get('1.0', tk.END)

        # Символы
        char_count = len(text) - 1  # -1 для учета символа новой строки
        self.char_count_var.set(f"Символов: {char_count}")

        # Слова
        words = text.split()
        word_count = len(words)
        self.word_count_var.set(f"Слов: {word_count}")


def main_tkinter():
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    # Для запуска PyQt5 версии используйте main()
    # Для запуска tkinter версии используйте main_tkinter()

    # Проверяем, установлен ли PyQt5
    try:
        from PyQt5.QtWidgets import QApplication

        main()  # Запускаем PyQt5 версию
    except ImportError:
        print("PyQt5 не установлен. Запускается версия на tkinter...")
        main_tkinter()  # Запускаем tkinter версию