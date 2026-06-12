import streamlit as st

def css_styling():
    """Add custom CSS for styling the portfolio"""
    st.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1a1a2e;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 1.6rem;
        color: #1a1a2e;
        border-bottom: 3px solid #4a90d9;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .contact-info {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin-bottom: 25px;
        font-size: 1rem;
        color: #333;
    }
    .highlight {
        background-color: #f7f9fc;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 4px solid #4a90d9;
    }
    .link-button {
        display: inline-block;
        padding: 10px 18px;
        background-color: #4a90d9;
        color: white !important;
        text-decoration: none;
        border-radius: 6px;
        margin: 5px;
        font-weight: 500;
        transition: background-color 0.3s ease;
    }
    .link-button:hover {
        background-color: #2f6fb8;
    }
    .skill-tag {
        display: inline-block;
        background-color: #eaf2fb;
        color: #2f6fb8;
        padding: 6px 14px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.9rem;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Shubham Kumar - Portfolio", page_icon=":technologist:", layout="wide")
    css_styling()

    st.markdown('<h1 class="main-title">Shubham Kumar</h1>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Research & Data Analysis Associate | NCGG, Government of India</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-info">
        <span>📧 Shubhamrawatk203@gmail.com</span>
        <span>📱 +91-8810325212</span>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.title("Portfolio Navigator")
    page = st.sidebar.radio("Go to",
        ["About Me", "Experience", "Education", "Projects", "Skills", "Achievements"])

    if page == "About Me":
        about_me()
    elif page == "Education":
        education()
    elif page == "Experience":
        experience()
    elif page == "Projects":
        projects()
    elif page == "Skills":
        skills()
    elif page == "Achievements":
        achievements()

def about_me():
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight">
    Computer Engineering graduate from Delhi Technological University (DTU) with experience in
    government programme support, policy research, data analysis, and web development. Currently
    working with the National Centre for Good Governance (NCGG), Government of India, contributing
    to research, monitoring & evaluation, stakeholder coordination, and programme implementation.
    Skilled in Python, SQL, and data visualization, with a strong analytical mindset and adaptability
    across multidisciplinary environments.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h3>Professional Profiles</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <a href="https://leetcode.com/CodingGeek2024" target="_blank" class="link-button">
        🧩 LeetCode Profile
        </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <a href="https://github.com/CodingGeek2024" target="_blank" class="link-button">
        💻 GitHub Profile
        </a>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <a href="https://www.linkedin.com/in/shubham-kumar-rawat-b69b1a19b/" target="_blank" class="link-button">
        🔗 LinkedIn Profile
        </a>
        """, unsafe_allow_html=True)

    st.markdown('<h3>Core Competencies</h3>', unsafe_allow_html=True)
    competencies = [
        "Problem Solving & Analytical Thinking", "Cross-functional Collaboration",
        "Technical Documentation", "Research & Report Writing", "Data Analysis & Interpretation",
        "Governance Evaluation", "Presentation & Communication", "Stakeholder Management",
        "Adaptability & Continuous Learning", "Quality-focused Execution"
    ]
    st.markdown("".join([f'<span class="skill-tag">{c}</span>' for c in competencies]), unsafe_allow_html=True)

    st.markdown('<h3>Interests & Hobbies</h3>', unsafe_allow_html=True)
    st.markdown("""
    - **Fitness & Strength Training** — regular gym workouts for discipline and a healthy lifestyle
    - **Outdoor Sports** — recreational activities promoting teamwork and strategic thinking
    - **Travel & Exploration** — exploring new places, cultures, and experiences
    """)

def education():
    st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    <h3>Bachelor of Technology (B.Tech) in Computer Engineering</h3>
    <b>Delhi Technological University (Formerly Delhi College of Engineering)</b><br>
    August 2019 – July 2023 | New Delhi, India<br>
    CGPA: 7.34/10 (73.4%)
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<h3>Relevant Coursework</h3>', unsafe_allow_html=True)
    courses = [
        "Artificial Intelligence", "Database Management Systems", "Object-Oriented Engineering",
        "Web Technology", "Data-Driven Decision Making", "Policy Research & Analysis",
        "Monitoring & Evaluation (M&E)", "Program Implementation & Evaluation",
        "Impact Assessment & Reporting", "Stakeholder Coordination", "Reporting & Documentation"
    ]
    st.markdown("".join([f'<span class="skill-tag">{c}</span>' for c in courses]), unsafe_allow_html=True)

    st.markdown('<h3>Certifications</h3>', unsafe_allow_html=True)
    st.markdown("""
    - [Crash Course on Python](https://www.coursera.org/account/accomplishments/certificate/3AWJHBS7KHH3) — Coursera
    - [Building Modern Python Applications on AWS](https://www.coursera.org/account/accomplishments/certificate/EDV2KUP3DLME) — Coursera
    """)

def experience():
    st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    <h3>Research & Data Analysis Associate (DEO)</h3>
    <b>National Centre for Good Governance (NCGG), DARPG, Government of India</b><br>
    <i>An autonomous institution under the Ministry of Personnel, Public Grievances and Pensions</i><br>
    September 2025 – Present | New Delhi
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Support policy research, programme planning, and Monitoring & Evaluation (M&E) activities through data collection, analysis, and structured reporting
    - Prepare concept notes, official correspondence, proposals, databases, programme records, and progress reports for senior government officials
    - Coordinate stakeholder engagements and capacity-building initiatives involving national and international participants
    - Contributed to the Right to Services (RTS) Maharashtra initiative by supporting service mapping and understanding administrative hierarchies across departments
    - Ensure accuracy, compliance, and timely submission of programme-related documentation and reports
    """)

    st.markdown("""
    <div class="highlight">
    <h3>Web Development Intern</h3>
    <b>Tripfox Travellers () (</b><br>
    March 2024 – May 2024
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Developed and maintained responsive web applications using JavaScript, ReactJS, and Node.js
    - Applied object-oriented programming principles to design scalable software solutions
    - Assisted in implementing CI/CD practices, contributing to improved deployment efficiency
    - Performed testing, debugging, and technical documentation to ensure software reliability and maintainability
    - Collaborated effectively with team members to deliver project requirements within specified timelines
    """)

    st.markdown("""
    <div class="highlight">
    <h3>IT Support Associate</h3>
    <b>Government Digital Service</b><br>
    2019 – 2022
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Supported citizen-facing digital platforms including Social Welfare, Women & Child Development (WCD), NSDL, and e-District Delhi services
    - Conducted data entry, verification, validation, and record management while maintaining confidentiality standards
    - Ensured timely and accurate processing of information to facilitate efficient public service delivery
    - Maintained data quality and compliance with operational guidelines
    """)

    st.markdown("""
    <div class="highlight">
    <h3>Brand Executive</h3>
    <b>Coding Blocks, Noida</b><br>
    October 2021 – December 2022
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Led campus outreach initiatives to strengthen student engagement and brand visibility
    - Planned and executed promotional campaigns to achieve organizational targets and KPIs
    - Facilitated awareness regarding internships, learning opportunities, and career development initiatives
    - Coordinated events and community-building activities within the student ecosystem
    """)

    st.markdown("""
    <div class="highlight">
    <h3>Volunteer Educator</h3>
    <b>Desh Ke Mentor Programme, Government of NCT Delhi</b><br>
    December 2022
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Mentored school students by providing academic guidance and career-related support
    - Encouraged informed decision-making regarding higher education and professional pathways
    - Contributed to initiatives aimed at improving educational awareness among students
    """)

def projects():
    st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    <h3>Portfolio Website</h3>
    <i>Python, Streamlit | October 2024 – November 2024</i>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Developed and deployed a responsive portfolio website showcasing academic projects, professional experiences, publications, and achievements
    - Designed user-friendly interfaces to improve accessibility and professional presentation
    - Hosted the application on Streamlit Cloud for public access
    - [View Repository](https://github.com/CodingGeek2024/Personal-Portfolio)
    """)

    st.markdown("""
    <div class="highlight">
    <h3>Mortgage Calculator Web Application</h3>
    <i>Python, Streamlit | December 2024</i>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Built an interactive financial calculator capable of computing mortgage payments and amortization schedules
    - Implemented financial computation logic with dynamic user inputs and automated calculations
    - Integrated data visualization features to enhance interpretability of financial outcomes
    - Utilized Pandas and Streamlit to deliver an intuitive user experience
    - [View Repository](https://github.com/CodingGeek2024)
    """)

    
    st.markdown("""
    <div class="highlight">
    <h3>Sales Management System</h3>
    <i>C++ | September 2021 – March 2022</i>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Designed a Sales Management System using C++ and Database Management System concepts
    - Documented network policies and procedures
    - Prioritized system maintenance and data integrity
    - [View Repository](https://github.com/CodingGeek2024/Developed-_C-_Project)
    """)

def skills():
    st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Programming Languages")
        for s in ["Python", "SQL", "JavaScript"]:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

        st.markdown("### Data Analytics & Visualization")
        for s in ["Microsoft Excel", "Power BI", "Tableau", "Streamlit", "Data Visualization", "Basic Statistics"]:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

        st.markdown("### Software Development")
        for s in ["ReactJS", "Node.js", "OOP", "Testing & Debugging", "Technical Documentation"]:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

    with col2:
        st.markdown("### Research & Governance")
        for s in ["Policy Research & Analysis", "Monitoring & Evaluation (M&E)", "Programme Implementation",
                   "Survey Analysis", "Stakeholder Coordination", "Impact Assessment", "Report Writing"]:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

        st.markdown("### Tools & Platforms")
        for s in ["MS Office Suite", "E-Office", "VS Code", "GitHub", "Google Drive"]:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

        st.markdown("### AI & Productivity Tools")
        for s in ["ChatGPT", "Claude AI", "Perplexity AI", "Emergent AI", "Bolt AI"]:
            st.markdown(f'<span class="skill-tag">{s}</span>', unsafe_allow_html=True)

def achievements():
    st.markdown('<h2 class="section-title">Achievements & Publications</h2>', unsafe_allow_html=True)

    st.markdown('<h3>Research & Publications</h3>', unsafe_allow_html=True)
    st.markdown("""
    - [ChatGPT & Google Bard AI: A Review](https://ieeexplore.ieee.org/document/10263706) — Published at IEEE ICICAT 2023 Conference, examining emerging generative AI technologies and their applications
    """)

    st.markdown('<h3>Technical Achievements</h3>', unsafe_allow_html=True)
    st.markdown("""
    - Solved 1000+ Data Structures & Algorithms problems on [LeetCode](https://leetcode.com/CodingGeek2024)
    """)

    st.markdown('<h3>Educational Achievements</h3>', unsafe_allow_html=True)
    st.markdown("""
    - Secured All India Rank 296 in JEE Main 2019
    - Secured All India Rank 1751 in JEE Advanced 2019
    """)

    st.markdown('<h3>Professional Contributions</h3>', unsafe_allow_html=True)
    st.markdown("""
    - [Leadership for 21st Century Women Professionals Programme** — Participated in the programme for the Delegation of Women Parliamentarians from Ethiopia, conducted by NCGG (November 2025)]( https://www.pib.gov.in/PressReleasePage.aspx?PRID=2238485&reg=6&lang=1)
    - [2nd Capacity Building Programme for Senior Civil Servants of Mauritius** — Contributed to the programme organized by NCGG (March 2026)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2189251&reg=3&lang=2)
        """)

    st.markdown('<h3>Leadership & Extracurricular</h3>', unsafe_allow_html=True)
    st.markdown("""
    **Decoder Coding Society, DTU** — Member | August 2019 – June 2023
    - Participated in coding contests, technical events, and collaborative learning initiatives
    - Strengthened problem-solving, teamwork, and analytical thinking through active involvement in the coding community
    """)

if __name__ == "__main__":
    main()