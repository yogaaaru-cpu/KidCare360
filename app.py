import streamlit as st
from datetime import datetime, date
from html import escape

# KidCare 360 — educational prototype
# Uses fictional sample data and Streamlit session state only.
# Not a production medical-record system.

st.set_page_config(
    page_title="KidCare 360 | Student Health",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------- Theme -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #07366B;
    --navy-dark: #052B57;
    --blue: #0875F5;
    --sky: #EAF4FF;
    --line: #D7E7F8;
    --text: #102F5E;
    --green: #11A875;
    --orange: #FF9900;
    --coral: #F43F5E;
}
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #EEF6FF; color: var(--text); }

header[data-testid="stHeader"] { height: 0; background: transparent; }
[data-testid="stToolbar"], [data-testid="stMainMenu"], .stDeployButton { display: none; }

.block-container { padding-top: .65rem; padding-bottom: 2rem; max-width: 1500px; }
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #07366B 0%, #05264D 100%);
    border-right: 1px solid #0A4B8E;
}
section[data-testid="stSidebar"] * { color: #FFFFFF; }
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { color: #D9E9FF; }
section[data-testid="stSidebar"] div[role="radiogroup"] { gap: 7px; }
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    border-radius: 10px; padding: 9px 11px; border: 1px solid transparent;
    font-weight: 800 !important; color: #FFFFFF !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label p,
section[data-testid="stSidebar"] div[role="radiogroup"] label span {
    color: #FFFFFF !important; font-weight: 800 !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: #0875F5; border-color: #56A5FF;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover { background: #104C88; }
h1, h2, h3 { color: #0A3267 !important; }
div[data-testid="stWidgetLabel"] p, .stTextInput label, .stSelectbox label,
.stDateInput label, .stTextArea label, .stNumberInput label {
    font-weight: 800 !important; color: #123967 !important;
}
div[data-testid="stMetric"] {
    background: #FFFFFF; border: 1px solid var(--line); border-radius: 14px;
    padding: 12px 15px; box-shadow: 0 3px 12px rgba(15, 61, 112, .04);
}
div[data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 12px; }
.hero {
    background: linear-gradient(120deg, #0875F5 0%, #07366B 72%);
    color: #FFFFFF; padding: 23px 27px; border-radius: 16px; margin-bottom: 17px;
    box-shadow: 0 6px 18px rgba(5, 43, 87, .12);
}
.hero h1 { color: #FFFFFF !important; margin: 0; font-size: 1.9rem; }
.hero p { color: #E7F3FF; margin: 6px 0 0 0; }
.kicker { font-size: .72rem; font-weight: 800; letter-spacing: 1.5px; color: #D5EBFF; }
.card {
    background: #FFFFFF; border: 1px solid #D7E7F8; border-radius: 14px;
    padding: 17px; min-height: 115px; box-shadow: 0 3px 12px rgba(15, 61, 112, .04);
}
.card h3 { margin: 4px 0 7px 0; font-size: 1.05rem; }
.card p { margin: 0; color: #54708F; font-size: .88rem; }
.pill { display: inline-block; padding: 4px 9px; border-radius: 99px; font-size: .75rem; font-weight: 800; }
.pill-green { background: #DDF8ED; color: #087A52; }
.pill-orange { background: #FFF0D4; color: #8A4A00; }
.pill-red { background: #FFE2E7; color: #B4233D; }
.section-head { margin: 14px 0 8px; font-weight: 800; color: #0A3267; font-size: 1.08rem; }
div.stButton > button {
    border-radius: 9px; font-weight: 700; border: 1px solid #C8DDF3;
}
div.stButton > button[kind="primary"] { background: #0875F5; border-color: #0875F5; }
.small-note { color: #5A7391; font-size: .82rem; }
.login-panel {
    background: white; border: 1px solid #D7E7F8; border-radius: 18px;
    padding: 25px; box-shadow: 0 8px 28px rgba(10, 50, 103, .08);
}
/* Keep the Logout button blue, including on hover */
[data-testid="stSidebar"] button {
    background-color: #1976D2 !important;
    color: white !important;
    border: 1px solid #1976D2 !important;
    transition: none !important;
}

[data-testid="stSidebar"] button:hover,
[data-testid="stSidebar"] button:focus,
[data-testid="stSidebar"] button:active {
    background-color: #1976D2 !important;
    color: white !important;
    border-color: #1976D2 !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------------- Demo data -------------------------
if "students" not in st.session_state:
    st.session_state.students = [
        {"id": "KC-001","card_number": "SC-1001", "name": "Ananya S", "grade": "6", "dob": date(2015, 4, 12),
         "gender": "Female", "school": "Demo School", "blood": "B+", "allergies": "Dust",
         "conditions": "No chronic conditions", "medications": "None recorded",
         "contact_name": "Parent/Guardian", "contact_phone": "000-000-0000",
         "instructions": "Contact parent/guardian if support is needed", "verified": "10 Oct 2026"},
        {"id": "KC-002","card_number": "SC-1002", "name": "Aarav K", "grade": "7", "dob": date(2014, 8, 3),
         "gender": "Male", "school": "Demo School", "blood": "O+", "allergies": "Strawberry",
         "conditions": "Asthma (demo record)", "medications": "None recorded",
         "contact_name": "Parent/Guardian", "contact_phone": "000-000-0000",
         "instructions": "Follow school emergency procedures", "verified": "25 Aug 2026"},
        {"id": "KC-003","card_number": "SC-1003", "name": "Diya R", "grade": "6", "dob": date(2015, 1, 29),
         "gender": "Female", "school": "Demo School", "blood": "A+", "allergies": "None listed",
         "conditions": "None listed", "medications": "None recorded",
         "contact_name": "Parent/Guardian", "contact_phone": "000-000-0000",
         "instructions": "Confirm details with authorized staff", "verified": "02 Sep 2026"},
        {"id": "KC-004","card_number": "SC-1004", "name": "Ishaan M", "grade": "8", "dob": date(2013, 11, 7),
         "gender": "Male", "school": "Demo School", "blood": "AB+", "allergies": "Peanuts (demo record)",
         "conditions": "None listed", "medications": "None recorded",
         "contact_name": "Parent/Guardian", "contact_phone": "000-000-0000",
         "instructions": "Use approved school procedures", "verified": "14 Sep 2026"},
        {"id": "KC-005","card_number": "SC-1005", "name": "Meera P", "grade": "7", "dob": date(2014, 6, 18),
         "gender": "Female", "school": "Demo School", "blood": "O-", "allergies": "None listed",
         "conditions": "None listed", "medications": "None recorded",
         "contact_name": "Parent/Guardian", "contact_phone": "000-000-0000",
         "instructions": "Contact parent/guardian if needed", "verified": "01 Oct 2026"},
    ]
if "change_log" not in st.session_state:
    st.session_state.change_log = [
        {"date": "10 Oct 2026", "changed_by": "Demo Admin", "section": "Profile",
         "change": "Sample record created"},
        {"date": "25 Sep 2026", "changed_by": "Demo Nurse", "section": "Allergies",
         "change": "Fictional allergy information reviewed"},
    ]
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "selected_id" not in st.session_state:
    st.session_state.selected_id = "KC-001"
if "form_step" not in st.session_state:
    st.session_state.form_step = 1

def student_by_id(student_id):
    return next((s for s in st.session_state.students if s["id"] == student_id), st.session_state.students[0])

def header(kicker, title, subtitle):
    st.markdown(
        f'<div class="hero"><div class="kicker">{escape(kicker)}</div>'
        f'<h1>{escape(title)}</h1><p>{escape(subtitle)}</p></div>',
        unsafe_allow_html=True
    )

def card(icon, title, desc, color):
    st.markdown(
        f'<div class="card" style="border-top:4px solid {color}">'
        f'<div style="font-size:1.6rem">{icon}</div><h3>{escape(title)}</h3>'
        f'<p>{escape(desc)}</p></div>', unsafe_allow_html=True
    )

# ------------------------- Demo login -------------------------
# These credentials are for the classroom prototype only.
# Do not use hard-coded passwords for a real student health system.
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "KidCare360!"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    left, right = st.columns(
        [1.05, 0.95],
        gap="large",
        vertical_alignment="center"
    )

    with left:
        st.image("kidcare_logo.png", width=245)
        st.markdown("## 💙 Welcome !")
        st.write("Sign in to explore the student health prototype.")

        with st.form("login_form"):
            username = st.text_input(
                "Username",
                placeholder="Enter username"
            )
            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter password"
            )
            submitted = st.form_submit_button(
                "Login →",
                type="primary",
                use_container_width=True
            )

        st.caption("Demo username: admin")
        st.caption("Demo password: KidCare360!")

    if submitted:
       if username.strip() == DEMO_USERNAME and password == DEMO_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.page = "Home"
        st.rerun()
    else:
        st.error(
            "Incorrect demo username or password. Please try again."
        )

    with right:
        st.image(
            "student_health_illustration.png",
            use_container_width=True
        )

    st.stop()

# ------------------------- Sidebar -------------------------
with st.sidebar:
    try:
        st.image("kidcare_logo.png", width=185)
    except Exception:
        st.markdown("## 💙 KidCare 360")
    st.caption("THE RIGHT INFORMATION AT THE RIGHT TIME")
    st.divider()
    st.markdown("### 🧭 Navigation")
    pages = ["Home", "Student Form", "Overall View", "Emergency View", "Previous Records"]
    current_index = pages.index(st.session_state.page) if st.session_state.page in pages else 0
    page_choice = st.radio("Navigation", pages, index=current_index, label_visibility="collapsed")
    if page_choice != st.session_state.page:
        st.session_state.page = page_choice
        st.rerun()
    if st.button("↪ Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.page = "Home"
        st.rerun()
    st.divider()
    st.markdown("#### 🛡️ Prototype status")
    st.caption("DEMO ENVIRONMENT")
    st.caption("Fictional records only • Session-only changes • No camera or cloud database")
    st.caption("KidCare 360 • Educational prototype")

page = st.session_state.page

# ------------------------- Home -------------------------
if page == "Home":
    header("SCHOOL HEALTH INFORMATION • EDUCATIONAL PROTOTYPE",
           "Welcome to KidCare 360", "The right information at the right time.")
    hour = datetime.now().hour
    greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 17 else "Good evening"
    st.success(f"💚 {greeting}! Use the options below to explore the student health prototype.")
    st.markdown('<div class="section-head">Choose an option to continue</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        card("🧑‍🎓", "Student Form", "Enter or review fictional student health details.", "#0875F5")
        if st.button("Open Student Form →", key="home_form", use_container_width=True):
            st.session_state.page = "Student Form"; st.rerun()
    with c2:
        card("👥", "Overall View", "Search and view the sample student profiles.", "#11A875")
        if st.button("Open Overall View →", key="home_overall", use_container_width=True):
            st.session_state.page = "Overall View"; st.rerun()
    c3, c4 = st.columns(2, gap="medium")
    with c3:
        card("🚨", "Emergency View", "Quickly review important demo emergency fields.", "#F43F5E")
        if st.button("Open Emergency View →", key="home_emergency", use_container_width=True):
            st.session_state.page = "Emergency View"; st.rerun()
    with c4:
        card("🕘", "Previous Records", "See example entries in the prototype change log.", "#7C3AED")
        if st.button("Open Previous Records →", key="home_history", use_container_width=True):
            st.session_state.page = "Previous Records"; st.rerun()
    st.info("Privacy note: this educational prototype uses fictional data. Do not enter real student medical information.")

# ------------------------- Student Form -------------------------

elif page == "Student Form":
    header(
        "STUDENT HEALTH RECORD",
        "Student Form",
        "Add a new fictional student or load an existing demo record."
    )

    # Keep the available student records
    students = st.session_state.students
    existing_ids = [s["id"] for s in students]

    # Helper: find a record using its internal app ID
    def get_student(student_id):
        for student in st.session_state.students:
            if student["id"] == student_id:
                return student
        return st.session_state.students[0]

    # Store form values in session state so we can clear or load them
    field_defaults = {
        "student_name_input": "",
        "card_number_input": "",
        "dob_input": date.today(),
        "grade_input": "6",
        "gender_input": "Not specified",
        "school_input": "",
        "blood_input": "Not provided",
        "conditions_input": "",
        "medications_input": "",
        "allergies_input": "",
        "contact_name_input": "",
        "contact_phone_input": "",
        "instructions_input": "",
    }

    for key, default_value in field_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

    # Load a student's information into the form
    def load_student(student):
        st.session_state.student_name_input = student.get("name", "")
        st.session_state.card_number_input = student.get("card_number", "")
        st.session_state.dob_input = student.get("dob", date.today())
        st.session_state.grade_input = student.get("grade", "6")
        st.session_state.gender_input = student.get(
            "gender", "Not specified"
        )
        st.session_state.school_input = student.get("school", "")
        st.session_state.blood_input = student.get(
            "blood", "Not provided"
        )
        st.session_state.conditions_input = student.get("conditions", "")
        st.session_state.medications_input = student.get("medications", "")
        st.session_state.allergies_input = student.get("allergies", "")
        st.session_state.contact_name_input = student.get("contact_name", "")
        st.session_state.contact_phone_input = student.get("contact_phone", "")
        st.session_state.instructions_input = student.get("instructions", "")

    # Start a completely blank new-student form
    def clear_student_form():
        for key, default_value in field_defaults.items():
            st.session_state[key] = default_value
        st.session_state.form_mode = "Add fictional student"
        st.session_state.selected_id = ""

    if "form_mode" not in st.session_state:
        st.session_state.form_mode = "Add fictional student"

    # Buttons to start fresh or load an existing record
    button_left, button_right = st.columns(2)

    button_left, button_right = st.columns(2)

    with button_left:
     st.markdown("**📝 Click here to add a new entry**")
     st.button(
         
        "➕ New Entry",
        key="new_student_button",
        on_click=clear_student_form,
        use_container_width=True,
    )


    with button_right:
        st.markdown("**Choose an existing student**")
        st.selectbox(
            "",
            existing_ids,
            key="form_selected_id",
            format_func=lambda sid: (
                f"{sid} — {get_student(sid)['name']}"
            ),
        )

        if st.button("📂 Load Selected Student", use_container_width=True):
            selected_student = get_student(
                st.session_state.form_selected_id
            )
            load_student(selected_student)
            st.session_state.selected_id = selected_student["id"]
            st.session_state.form_mode = "Edit selected demo student"
            st.rerun()

    if st.session_state.form_mode == "Add fictional student":
        st.info("🆕 New student mode — the form should be blank.")
    else:
        st.info("✏️ Edit mode — check the loaded student's details.")

    # One form containing ALL student information
    with st.form("complete_student_form"):
        st.subheader("👤 Personal Information")

        name = st.text_input(
            "Student Name",
            key="student_name_input",
        )
        card_number = st.text_input(
            "Student ID Card Number",
            key="card_number_input",
            placeholder="Example: SC-1001",
        )

        dob = st.date_input(
            "Date of Birth",
            key="dob_input",
            min_value=date(1990, 1, 1),
            max_value=date.today(),
        )

        grade = st.selectbox(
            "Class / Grade",
            ["6", "7", "8"],
            key="grade_input",
        )

        gender = st.selectbox(
            "Gender",
            [
                "Not specified",
                "Female",
                "Male",
                "Prefer not to say",
            ],
            key="gender_input",
        )

        school = st.text_input(
            "School Name",
            key="school_input",
        )

        st.divider()
        st.subheader("🩺 Medical History")

        blood = st.selectbox(
            "Blood Group",
            [
                "Not provided", "A+", "A-", "B+", "B-",
                "AB+", "AB-", "O+", "O-",
            ],
            key="blood_input",
        )

        conditions = st.text_area(
            "Medical Conditions",
            key="conditions_input",
        )

        medications = st.text_area(
            "Current Medications (demo only)",
            key="medications_input",
        )

        st.divider()
        st.subheader("⚠️ Allergies")

        allergies = st.text_area(
            "Known Allergies",
            key="allergies_input",
        )

        st.caption(
            "Prototype only. This form does not provide medical advice "
            "or emergency treatment."
        )

        st.divider()
        st.subheader("📞 Emergency Contact")

        contact_name = st.text_input(
            "Parent / Guardian",
            key="contact_name_input",
        )

        contact_phone = st.text_input(
            "Emergency Contact Number",
            key="contact_phone_input",
        )

        instructions = st.text_area(
            "Special Instructions",
            key="instructions_input",
        )

        save_record = st.form_submit_button(
            "💾 Save Student Record",
            type="primary",
            use_container_width=True,
        )

    # Save all fields together
    if save_record:
        if not name.strip():
            st.error("Please enter a fictional student name.")
        elif not card_number.strip():
            st.error("Please enter a Student ID Card Number.")
        else:
            # Prevent duplicate card numbers
            duplicate_card = any(
                s.get("card_number", "").strip().casefold()
                == card_number.strip().casefold()
                and s["id"] != st.session_state.selected_id
                for s in st.session_state.students
            )

            # In new-student mode, check all existing records
            if st.session_state.form_mode == "Add fictional student":
                duplicate_card = any(
                    s.get("card_number", "").strip().casefold()
                    == card_number.strip().casefold()
                    for s in st.session_state.students
                )

            if duplicate_card:
                st.error(
                    "That Student ID Card Number is already in use. "
                    "Please enter a different number."
                )
            else:
                record_details = {
                    "card_number": card_number.strip(),
                    "name": name.strip(),
                    "dob": dob,
                    "grade": grade,
                    "gender": gender,
                    "school": school.strip(),
                    "blood": blood,
                    "conditions": conditions,
                    "medications": medications,
                    "allergies": allergies,
                    "contact_name": contact_name.strip(),
                    "contact_phone": contact_phone.strip(),
                    "instructions": instructions,
                    "verified": date.today().strftime("%d %b %Y"),
                }

                if st.session_state.form_mode == "Add fictional student":
                    used_numbers = [
                        int(s["id"].split("-")[1])
                        for s in st.session_state.students
                        if s.get("id", "").startswith("KC-")
                        and s["id"].split("-")[1].isdigit()
                    ]
                    new_num = max(used_numbers, default=0) + 1
                    new_id = f"KC-{new_num:03d}"

                    new_record = {
                        "id": new_id,
                        **record_details,
                    }

                    st.session_state.students.append(new_record)
                    st.session_state.selected_id = new_id
                    change = "Added fictional demo student"

                else:
                    selected_id = st.session_state.selected_id
                    selected_student = get_student(selected_id)
                    selected_student.update(record_details)
                    change = "Updated fictional demo record"

                st.session_state.change_log.insert(
                    0,
                    {
                        "date": date.today().strftime("%d %b %Y"),
                        "changed_by": "Demo User",
                        "section": "Student Form",
                        "change": change,
                    },
                )

                st.success("Student record saved for this demo session.")

                # Prepare a blank form for the next new student
                clear_student_form()
                st.rerun()

    st.caption(
        "Demo note: records are held in Streamlit session state, "
        "not saved to a permanent database."
    )

# ------------------------- Overall View -------------------------
elif page == "Overall View":
    header("STUDENT DIRECTORY", "Overall View", "Search the fictional student directory and preview a record.")
    search_col, grade_col = st.columns([2, 1])
    with search_col:
        query = st.text_input("Search by name or student ID", placeholder="e.g. Ananya or KC-001")
    with grade_col:
        grade_filter = st.selectbox("Filter by grade", ["All grades", "6", "7", "8"])
    filtered = [s for s in st.session_state.students
                if (query.lower() in s["name"].lower() or query.lower() in s["id"].lower())
                and (grade_filter == "All grades" or s["grade"] == grade_filter)]
    m1, m2, m3 = st.columns(3)
    m1.metric("👩‍🎓 Demo students", len(st.session_state.students))
    m2.metric("🎓 Grades", "6–8")
    m3.metric("🔒 Cloud connections", "0")
    st.markdown('<div class="section-head">Student records</div>', unsafe_allow_html=True)
    st.dataframe([{"Internal Record ID": s["id"],"Student ID Card Number": s.get("card_number", ""), "Student": s["name"], "Class": s["grade"],
                   "Blood Group": s["blood"], "Last Verified": s["verified"]} for s in filtered],
                 hide_index=True, width="stretch", height=240)
    if not filtered:
        st.warning("No matching demo students. Try a different search or grade.")
    else:
        st.markdown('<div class="section-head">Choose student to preview</div>', unsafe_allow_html=True)
        selected = st.selectbox("Choose student to preview",
                                [s["id"] for s in filtered],
                                format_func=lambda sid: f"{student_by_id(sid)['name']}  •  Grade {student_by_id(sid)['grade']}  •  {sid}",
                                label_visibility="collapsed")
        st.session_state.selected_id = selected
        chosen = student_by_id(selected)
        st.markdown(f"""<div class="card">
        <h3>👤 {escape(chosen['name'])} <span class="pill pill-green">Demo profile</span></h3>
        <p><b>Student ID:</b> {escape(chosen['id'])} &nbsp; • &nbsp; <b>Grade:</b> {escape(chosen['grade'])}
        &nbsp; • &nbsp; <b>Blood group:</b> {escape(chosen['blood'])}</p>
        <p style="margin-top:8px"><b>Known allergies:</b> {escape(chosen['allergies'])}</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Open Emergency View →", type="primary"):
            st.session_state.page = "Emergency View"; st.rerun()

# ------------------------- Emergency View -------------------------
elif page == "Emergency View":
    header("QUICK ACCESS • DEMO ONLY", "Emergency View", "Key fields shown for a fictional student. Follow school emergency procedures.")
    student_ids = [s["id"] for s in st.session_state.students]
    selected = st.selectbox("Choose student", student_ids,
                            index=student_ids.index(st.session_state.selected_id) if st.session_state.selected_id in student_ids else 0,
                            format_func=lambda sid: f"{student_by_id(sid)['name']} — {sid}")
    st.session_state.selected_id = selected
    s = student_by_id(selected)
    st.error("🚨 Emergency information — fictional prototype record")
    st.markdown(f"### {escape(s['name'])}  ·  Grade {escape(s['grade'])}  ·  {escape(s['id'])}")
    a, b = st.columns(2)
    with a:
        card("⚠️", "Known Allergies", s["allergies"], "#F43F5E")
        card("🩺", "Medical Conditions", s["conditions"], "#11A875")
        card("💊", "Current Medications", s["medications"], "#0875F5")
    with b:
        card("🩸", "Blood Group", s["blood"], "#FF9900")
        card("📞", "Emergency Contact", f"{s['contact_name']} · {s['contact_phone']}", "#7C3AED")
        card("📝", "Special Instructions", s["instructions"], "#10A7A0")
    st.caption(f"Last verified in demo: {s['verified']}")
    st.warning("This prototype does not contact emergency services and must not replace school health protocols or professional medical care.")

# ------------------------- Previous Records -------------------------
elif page == "Previous Records":
    header("AUDIT TRAIL • EXAMPLE DATA", "Previous Record Changes", "Illustrative change history for the educational prototype.")
    selected = st.selectbox("Choose student", [s["id"] for s in st.session_state.students],
                            index=[s["id"] for s in st.session_state.students].index(st.session_state.selected_id)
                                  if st.session_state.selected_id in [s["id"] for s in st.session_state.students] else 0,
                            format_func=lambda sid: f"{student_by_id(sid)['name']} — {sid}")
    st.session_state.selected_id = selected
    s = student_by_id(selected)
    st.markdown(f'<div class="card"><h3>👤 {escape(s["name"])}</h3><p>Grade {escape(s["grade"])} &nbsp; • &nbsp; ID {escape(s["id"])}</p></div>',
                unsafe_allow_html=True)
    st.markdown('<div class="section-head">Change history</div>', unsafe_allow_html=True)
    st.dataframe(st.session_state.change_log, hide_index=True, width="stretch", height=300)
    st.caption("These are session-level example entries, not a secure or permanent audit log.")

st.markdown("---")
st.markdown('<p class="small-note">💙 KidCare 360 • The Right Information at the Right Time • Educational prototype using fictional records only.</p>',
            unsafe_allow_html=True)
