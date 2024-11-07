import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def write_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def modify_data(data):
    # Find the indices of the relevant columns
    header = data[0]
    binder_name_idx = header.index("Binder Name")
    set_code_idx = header.index("Set code")
    set_name_idx = header.index("Set name")
    binder_type_idx = header.index("Binder Type")

    # Filter the data based on the new criteria
    filtered_data = [row for row in data if row[binder_name_idx] != "Italian Legends" and row[set_code_idx] != "LEGI" and row[set_name_idx] != "Legends Italian" and row[binder_type_idx] != "list"]
    # Collect some stats
    total_rows = len(data)
    removed_rows = total_rows - len(filtered_data)
    
    italian_legends_count1 = 0
    italian_legends_count2 = 0
    italian_legends_count3 = 0

    for row in data:
        if row[binder_name_idx] == "Italian Legends":
            italian_legends_count1 += 1
        elif "LEGI" in row[set_code_idx]:
            italian_legends_count2 += 1
        elif "Legends Italian" in row[set_name_idx]:
            italian_legends_count3 += 1
    combined_count = italian_legends_count1 + italian_legends_count2 + italian_legends_count3
    list_count = sum(1 for row in data if row[1] == "list")
    
    print(f"Total rows: {total_rows}")
    print(f"Removed rows: {removed_rows}")
    print(f"'Italian Legends': {combined_count}")
    print(f"'list': {list_count}")
    
    modified_data = filtered_data
    return modified_data

def main(input_file='input.csv', output_file='manabox_to_archidekt_output.csv'):
    # Read the CSV file
    data = read_csv(input_file)
    
    # Modify the data
    modified_data = modify_data(data)
    
    # Write the modified data to a new CSV file
    write_csv(output_file, modified_data)

if __name__ == "__main__":
    main()