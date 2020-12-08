import matplotlib.pyplot as plt
import numpy as np
import regex as re

def analysis():
    survey = np.loadtxt("survey_data.csv", delimiter=",", dtype=str)
    survey = survey[1:,:]

    # gender = survey[:,1]
    # uniques = sorted(list(set(gender)))
    # print(uniques)

    # for x, i in enumerate(survey[:,1]):
    #     index = uniques.index(i)
    #     if index == 3:
    #         survey[x,1] = 1
    #     elif index == 1:
    #         survey[x,1] = 2
    #     else:
    #         survey[x,1] = 0
    
    # for i in survey[:,1]:
    #     print(type(i))


    # attribute analysis
    col = survey[:,14]
    
    # overall analysis
    categories, counts = np.unique(col, return_counts=True)
    for y, i in enumerate(categories):
        print(f'{i} -> {counts[y]}')

    # mixed analysis
    mixed_dict = {i: 0 for i in ["mixed", "nonmixed"]}
    mixed_list = []
    nonmixed_list = []
    
    for i in col:
        # print(i)
        cha = [c for c in i]
        if ";" in cha:
            mixed_dict["mixed"] += 1
            mixed_list.append(i)
        else:
            mixed_dict["nonmixed"] += 1
            nonmixed_list.append(i)

    print(mixed_dict)
    print("\n")
    print("-"*5 + "MIXED" + "-"*5)
    ca, co = np.unique(mixed_list, return_counts=True)
    for x, i in enumerate(ca):
        print(f'{i} -> {co[x]}')

    print("-"*5 + "NONMIXED" + "-"*5)
    ca2, co2 = np.unique(nonmixed_list, return_counts=True)
    for x, i in enumerate(ca2):
        print(f'{i} -> {co2[x]}')

            

    #unique = {set(devices.): 0}
    #print(unique)
        

# exploratory data analysis
def load_data():
    survey = np.loadtxt("survey_data.csv", delimiter=",", dtype=str)

    # timestamp
    timestamp = survey[1:,0]

    # gender
    genders = survey[1:,1]
 
    # ages
    ages = survey[1:,2]
    
    # courses
    courses = survey[1:,3]

    # semester
    semesters = survey[1:,4]

    # quantity
    quantity = survey[1:,5]

    # quality 
    quality = survey[1:,6]

    # device
    devices = survey[1:,7]

    # application
    app = survey[1:,8]

    # method
    methods = survey[1:,9]

    # time of notetaking
    times = survey[1:,10]

    # place of notetaking
    place = survey[1:,11]

    return (genders, ages, courses, semesters, quantity, quality, devices, app, methods, times, place)

def see(data, i):
    print(data[i])
    print(data[i].shape)
    print("\n")
    print(np.unique(data[i], return_counts=True))

# plotting each quantitative attribute
def genders():
    categories = ["Male", "Females", "Other"]
    counts = [38, 32, 2]

    print()

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Gender Distribution", fontweight='bold')
    # axes.set_xlabel("Genders", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories)

    # plt.savefig("genders.pdf")

def ages():
    categories = ["17-20", "21-25","26-30", "30+"]
    counts = [15, 45, 8, 4]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Age Distribution", fontweight='bold')
    # axes.set_xlabel("Age Groups", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories)

    plt.savefig("ages.pdf")

def courses():
    categories = ["BSc DS", "BSc DDIT", "BSc GBI", "BSc SD", "MSc CS", "MSc SD", "MSc DIM"]
    counts = [30,2,5,18,7,4,5]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Course Distribution", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories, Rotation=30, fontsize=8)

    plt.savefig("courses.pdf")

    # add legends

def semesters():
    categories = ["1", "3", "5", "Masters"]
    counts = [37, 23, 9, 3]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Semester Distribution", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories)

    plt.savefig("semesters.pdf")

def quantity():
    categories = ["1", "2", "3", "4", "5"]
    counts = [13,23,14,20,2]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Quantity of Notes Distribution", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories)

    plt.savefig("quantity.pdf")

def quality():
    categories = ["1", "2", "3", "4", "5"]
    counts = [9, 16, 26, 17, 4]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Quality of Notes Distribution", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories)

    plt.savefig("quality.pdf")

def methods():
    categories = ["Typing", "Writing","S-T-T", "Other"]
    counts = [62, 14, 1, 0]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Distribution of Method of Notetaking", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories, Rotation=30, fontsize=8)

    plt.savefig("methods.pdf")

def time():
    categories = ["Before", "During", "After"]
    counts = [47.23, 87.5, 18.05]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Distribution of Time of Notetaking", fontweight='bold')
    #axes.set_xlabel("Time of notetaking relative to lecture", style='italic')
    axes.set_ylabel("(%)")
    
    axes.set_xticklabels(categories, Rotation=30, fontsize=8)

    plt.savefig("time_of_notetaking.pdf")

def place():
    categories = ["ITU", "Home", "Public", "Other"]
    counts = [70.83, 76.38, 8.34, 4.16]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Distribution of Place of Notetaking", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    axes.set_ylabel("(%)")
    
    axes.set_xticklabels(categories, Rotation=30, fontsize=8)

    plt.savefig("place_of_notetaking.pdf")

def devices():
    categories = ["Laptop/PC", "Tablet", "Paper", "Other"]
    counts = [64, 5, 25, 4]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Distribution of Place of Notetaking", fontweight='bold')
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories, Rotation=30, fontsize=8)

    #plt.savefig("devices.pdf")

def app():
    categories = ["Notion", "OneNote", "Google Docs", "Evernote", "Word", "Other", "None"]
    counts = [4, 27, 4, 7, 15, 8, 10]

    fig = plt.figure(figsize=(4,3))

    axes = fig.add_axes([0.15,0.15,0.7,0.7])

    axes.bar(categories, counts, color="blue", alpha=0.4)
    axes.set_title("Distribution of Digital Notetaking Applications", fontweight='bold', fontsize=10)
    # axes.set_xlabel("ITU Courses", style='italic')
    # axes.set_ylabel("Amount")
    
    axes.set_xticklabels(categories, Rotation=30, fontsize=6)

    #plt.savefig("applications.pdf")


def explore():
    # survey = load_data()
    # see(survey, 7)
    analysis()

def main():
    # save all figures into the current directory
    # genders()
    # ages()
    # courses()
    # semesters()
    # quantity()
    # quality()
    # methods()
    # time()
    place()
    # devices()
    # app()
    print('Done')

# explore()
main()




