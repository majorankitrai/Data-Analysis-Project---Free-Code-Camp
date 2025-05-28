import pandas as pd

column_name = ['Age','workclass','fnlwgt','education','education-ntus','occupation',
                'relationship','race','sex','capital-gain','capital-loss','hours-per-week',
                'native-country','income']
df = pd.read_csv("C:\\Users\\admin\\Desktop\\project_pandas\\adult.csv",header = None,names= column_name)
#print(df.head(5))

# 1.Race count
race_count = df['race'].value_counts()
#print(race_count)

# 2.Average age of men
# Strip and clean all column names and string data
# Clean column names
df.columns = df.columns.str.strip()

# Clean 'sex' column and make lowercase
df['sex'] = df['sex'].astype(str).str.strip().str.lower()

# Clean Age column: remove non-numeric and convert to int
df['Age'] = df['Age'].astype(str).str.strip()
df = df[df['Age'].apply(lambda x: x.isnumeric())]
df['Age'] = df['Age'].astype(int)

# Calculate average age
average_men_age = round(df[df['sex'] == 'male']['Age'].mean(), 1)
print("Average age of men:", average_men_age)

# What is the percentage of people who have a Bachelor's degree?
num_bachelour = len(df[df['education']=='Bachelors'])
total_num = len(df['education'])
percentage_of_people = round((num_bachelour/total_num)*100.0,1)
print(percentage_of_people)

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

num_percent_higher = len(higher_education[higher_education == '>50k'])
higher_education_rich = round(num_percent_higher/len(higher_education)*100.0,1)
print(higher_education_rich)

num_percent_lower = len(df[df['lower_education']=='>50k'])
lower_education_rich = round(num_percent_lower/len(lower_education)*100.0,1)
print(lower_education_rich)

#What is the minimum number of hours a person works per week?
min_hour_work = df['hours-per-week'].min()
print(min_hour_work)

#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_worker = df[df['hours-per-week'] == min_hour_work]
rich_percent = round(len(num_min_worker[num_min_worker.salary =='>50k'])/len(num_min_worker)*100,1)
print(rich_percent)

#What country has the highest percentage of people that earn >50K and what is that percentage?
countyr_count = df['native-country'].value_counts()
country_rich_count = df[df['salary']=='>50k']['native-country'].value_counts()

highest_country_count = round((country_rich_count/countyr_count*100.0).max(),1)
print(highest_country_count)

# Identify the most popular occupation for those who earn >50K in India.
people_of_india = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
occupation_counts = people_of_india['occupation'].value_counts()
top_IN_occupation = occupation_counts.idxmax()

print(top_IN_occupation)

