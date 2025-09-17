from ollama import chat
from ollama import ChatResponse

import re
def ask_deepseek(input_content, system_prompt, deep_think = True, print_log = True):
    response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': input_content}
    ])
    response_text = response['message']['content']
    if print_log: print(response_text)

    think_texts = re.findall(r'<think>(.*?)</think>', response_text, flags=re.DOTALL)
    think_texts = "\n\n".join(think_texts).strip()
    clean_response = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL).strip()

    return clean_response if not deep_think else (clean_response, think_texts)

system_prompt = '''You are an attendant who will only accept questions, and you will only answer the questions whose answers are found in the following text:
Fatec Entrance Exam – Explanatory Guide (1st Semester 2026)
1. General Information
The Vestibular is the official selection process used to admit candidates into the Technology Colleges of the State of São Paulo (Fatecs). Admission is based on performance in an in-person written exam.
Eligible applicants include those who have completed or are completing high school by the enrollment date, through regular education, national certification exams (ENEM or ENCCEJA), or Youth and Adult Education (EJA). Proper documentation (transcripts and certificates) must be presented at enrollment.
There is no minimum age requirement, except for the Radiology Higher Technology Course, which requires students to be at least 18 years old by the fourth semester to participate in laboratory practice classes, as determined by CNE/CEB regulations.
The process is organized by Fundação de Apoio à Tecnologia (FAT), which provides a secure and transparent digital system for all phases of the selection process.

2. Calendar of Activities
September 15 – November 7, 2025 (until 3 p.m.): Online application via vestibular.fatec.sp.gov.br
.
December 9, 2025 (from 3 p.m.): Release of test location information.
December 14, 2025 (1 p.m.): Written exam date.
December 17, 2025 (from 3 p.m.): Publication of the official answer key.
January 19, 2026 (from 3 p.m.): Release of the general ranking list and first call of admitted candidates.
January 20–22, 2026: Online enrollment for candidates admitted in the first call.
January 26, 2026 (from 3 p.m.): Release of the second call list.
January 27–29, 2026: Online enrollment for candidates admitted in the second call.
Candidates are fully responsible for monitoring all dates, results, and enrollment procedures. No extensions or late document submissions will be accepted.

3. Application
Applications must be completed exclusively online at the official website. Each applicant must:
Provide complete and accurate personal information.
Indicate their desired course and shift (day, evening, or night).
Pay the application fee through the available banking methods, unless granted an exemption or reduction.
Applicants are responsible for ensuring all information is correct. Any incomplete, inaccurate, or inconsistent data may result in disqualification.

4. Written Exam
The exam will be held in person on December 14, 2025, at 1 p.m.
It consists of 54 multiple-choice questions covering:
Portuguese Language and Literature
Mathematics
History
Geography
Physics
Chemistry
Biology
English Language
Logical Reasoning
In addition, candidates must write a short essay, which is a mandatory part of the evaluation.
Candidates must arrive at the assigned location with:
An official photo ID.
A black or blue ballpoint pen.
Electronic devices, notes, or communication during the exam are strictly prohibited.

5. Scoring and Classification
The final score will be calculated as follows:
Multiple-choice questions: Each correct answer adds one point.
Essay: Scored separately and considered essential for classification.
The final classification list will rank candidates according to their overall performance.
Ties will be resolved based on:
Higher essay score.
Higher Portuguese Language score.
Higher Mathematics score.
Older age (priority given to the oldest candidate).

6. Enrollment
Enrollment will be conducted exclusively online, through the system https://siga.cps.sp.gov.br/matricula/matricularemota.aspx
.
Admitted candidates must submit digital copies of the required documents, which include:
High school completion certificate or equivalent.
Academic transcript.
Birth or marriage certificate.
ID card and CPF (taxpayer number).
Proof of address.
One 3x4 photo (recent).
Failure to submit any required document will result in loss of the spot.

7. Calls and Waiting List
First call: January 19, 2026.
Second call: January 26, 2026.
Candidates not admitted in the first or second call may still have the chance to enroll if additional spots become available. This depends on withdrawals or uncompleted registrations. Fatec units will provide guidance on procedures for remaining vacancies.

8. Final Provisions
All official communications will be made through the websites vestibular.fatec.sp.gov.br
 and www.cps.sp.gov.br
.
It is the candidate’s responsibility to follow updates, announcements, and deadlines.
Situations not covered in this document will be resolved by the organizing committee, following the applicable regulations.'''
perguntas = ['Who can apply for the Fatec Araraquara entrance exam?',
             'Is there a minimum age requirement to apply for a course at Fatec Araraquara?',
             'How does the selection process work specifically at Fatec Araraquara?',
             'What is the schedule for the 1st semester of 2026 exam at Fatec Araraquara?']

for pergunta in perguntas:
    resposta = ask_deepseek(pergunta, system_prompt, deep_think=False)
    print(resposta)
