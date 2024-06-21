from bs4 import BeautifulSoup
import os

def extract_courses_and_save(file_path, output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Use Beautiful Soup to parse the HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # Find all course entries in the slick area
    course_entries = soup.find_all('div', class_='slick-area__item')
    courses = []

    for course in course_entries:
        # Extract the course title and link
        course_link = course.find('a', class_='ck-curso')
        if course_link:
            title = course_link.find('h6', class_='ssp-card-curso__title').text.strip() if course_link.find('h6', class_='ssp-card-curso__title') else 'No title'
            link = course_link['href'].strip()
            courses.append(f"{title}: {link}\n")

    # Save the courses to a text file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(courses)
    print(f"Courses saved to: {output_path}")

if __name__ == '__main__':
    # Input and output paths
    file_path = 'data/subCursosBelezaEestetica.html'
    output_path = 'data/cursosBelezaEestetica.txt'
    extract_courses_and_save(file_path, output_path)
