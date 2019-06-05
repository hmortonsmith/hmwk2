import csv
# PART II
# transform imdb data
    # only select films from later than 2010
    # only select movies
    # only select movie primary title
    # remove enddate and isadult fields


def transform_imdb_with_filipes_criteria(file_name, type, year, new_transformed_file_name):
    new_user_data = []
    try:
        # read csv, and find all data that fits criteria 1 and 2
        with open(file_name, newline='') as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')
            for row in csvreader:
                if row[0] == type and int(row[4]) >= int(year):
                    transformed_row = []
                    transformed_row.append(row[0])
                    transformed_row.append(row[1].title())
                    transformed_row.append(row[4])
                    transformed_row.append(row[6])
                    transformed_row.append(row[7])
                    new_user_data.append(transformed_row)

        new_file = open(new_transformed_file_name, 'w', newline='')
        with new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(new_user_data)
    except FileNotFoundError as error_message:
        print(error_message)
        print('Check file exists dummy!')

    finally:
        print('All done')


#transform_imdb_with_filipes_criteria('imdb.csv', 'movie', 2015, 'transformed_imdb_data1.csv')


# PART II
def transform_imdb_with_my_criteria(file_name, genre, type, year, new_transformed_file_name):
    new_user_data = []
    try:
        # read csv, and find all data that fits criteria 1 and 2
        with open(file_name, newline='') as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')
            for row in csvreader:
                if genre in row[7] and int(row[4]) >= int(year) and row[0] == type:
                    transformed_row = []
                    transformed_row.append(row[0])
                    transformed_row.append(row[1].title())
                    transformed_row.append(row[4])
                    if 'Horror' in row[7]:
                        transformed_row.append('NOT FOR SHAUN!')
                    else:
                        transformed_row.append('----')
                    transformed_row.append(row[6])
                    transformed_row.append(row[7])
                    new_user_data.append(transformed_row)

        new_file = open(new_transformed_file_name, 'w', newline='')
        with new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(new_user_data)
    except FileNotFoundError as error_message:
        print(error_message)
        print('Check file exists dummy!')

    finally:
        print('All done')


transform_imdb_with_my_criteria('imdb.csv', 'Comedy', 'movie', 2012, 'transformed_imdb_data2.csv')
