import tkinter as tk
from tkinter import scrolledtext
import re

def update_list(main_text_box, match_text_box, output_text_box):
    main_text = main_text_box.get("1.0", tk.END).strip()
    match_text = match_text_box.get("1.0", tk.END).strip()
    
    main_list = main_text.splitlines()
    match_list = match_text.splitlines()
    
    match_set = set(entry.split(":")[0].strip() for entry in match_list)
    
    updated_list = []
    trimmed_count = 0
    for line in main_list:
        # Extract card name by removing leading quantity and everything after the first "(" and "["
        card_name = re.sub(r'^\d+x\s+', '', line).split("(")[0].split("[")[0].strip()
        if card_name in match_set:
            trimmed_count += 1
            if "[" in line:
                line = line[:line.index("[")] + "[Trimmed{noDeck}{noPrice}]"
            else:
                line += " [Trimmed{noDeck}{noPrice}]"
        updated_list.append(line)
    
    output_text = "\n".join(updated_list)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, output_text)
    
    return trimmed_count

# Create main window
TEXT_BOX_WIDTH = 90
TEXT_BOX_HEIGHT = 12

window = tk.Tk()
window.title("Deckcheck Trim Helper")
window.geometry("775x700")

# Main List Label and Text Box
main_label = tk.Label(window, text="Paste Full Archidekt Import List Here:")
main_label.pack()
main_text_box = scrolledtext.ScrolledText(window, width=TEXT_BOX_WIDTH, height=TEXT_BOX_HEIGHT)
main_text_box.pack()

# Match List Label and Text Box
match_label = tk.Label(window, text="Paste Deckcheck remove List Here:")
match_label.pack()

match_text_box = scrolledtext.ScrolledText(window, width=TEXT_BOX_WIDTH, height=TEXT_BOX_HEIGHT)
match_text_box.pack()

# Output Label and Text Box
output_label = tk.Label(window, text="Replace Archidekt Import list with this:")
output_label.pack()
output_text_box = scrolledtext.ScrolledText(window, width=TEXT_BOX_WIDTH, height=TEXT_BOX_HEIGHT)
output_text_box.pack()

# Update Button
def on_update_button_click():
    trimmed_count = update_list(main_text_box, match_text_box, output_text_box)
    message_label.config(text=f"{trimmed_count} cards trimmed")

update_button = tk.Button(window, text="Trim List", command=on_update_button_click)
update_button.pack()

# Message Label
message_label = tk.Label(window, text="")
message_label.pack()

# Run the application
window.mainloop()
