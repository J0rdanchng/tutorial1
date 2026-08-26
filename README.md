Use this repository to complete and submit your tutorial answers. 
If you need to upload images, code, or other supporting files, please add them to this repository as needed.

# Declaration

## AI Use Declaration

Students may be called for an interview to explain and demonstrate their understanding of the submitted work. Failure to do so may result in disciplinary action.

- [ ] AI assistance (such as GitHub Copilot or ChatGPT) **was properly used** in preparing this submission.
- [ ] AI assistance **was not used** in preparing this submission.

### If AI was used, briefly describe how it assisted you

> Your response here. If not used, leave blank or write "Not applicable."

## Plagiarism Declaration

- [ ] I declare that this submission is my own work and does not contain plagiarized content from other sources.

# Tutorial

## Q1

### Part (a)

mkdir hello-world
mkdir hello-world/project
rm -r hello-world

## Part (b)
The ls -l command displays a detailed list of files and folders in long format, showing permissions, owners, sizes, and dates.

## Q2

cd ~
ln -s /bin/ls myls
./myls -l

# Q3 
## Part (c)

![alt text](<Active SSH session-3.png>)


### (d) Transfer `hello.txt`

I exited the remote server and created the file locally:

```bash
exit
printf "Hello from Jordan\n" > hello.txt
ls -l hello.txt
```

I copied it to my home directory on `stu` through the jump host:

```bash
scp -J jordan33@sjump.comp.nus.edu.sg hello.txt jordan33@stu.comp.nus.edu.sg:~
```

I connected to `stu` again and verified that the file had arrived:

```bash
ssh -J jordan33@sjump.comp.nus.edu.sg jordan33@stu.comp.nus.edu.sg
ls -l hello.txt. 
```


## Q5: UX Reflection

### Psychology
Question: How does my portfolio create a positive first impression?

Answer: My page uses a clear heading with my name and a short description at the top, & the clean layout and consistent sections will help people understand that it is a professional student portfolio

### Usability
Question: How easily can an interviewer find key information?

Answer: My page separates education, skills, projects, and contact information into clearly titled section,so an interviewer will be able to scan the headings and locate the information they need without searching through a long paragraph.

### Design
Question: Is the visual hierarchy clear?

Answer: Each section is placed in a separate card with spacing and headings. The dark-mode button is visible at the top, and the text has enough contrast against the background to remain readable.

### Copywriting
Question: Is my introduction clear and concise?

Answer: The introduction briefly explains that I am a student interested in technology, web development, and problem-solving, which avoids unnecessary long sentences and gives visitors a quick overview.

### Analysis
Question: How would I evaluate whether the portfolio works well?

Answer: I would ask classmates or an interviewer to find my skills and projects, then observe whether they can do so quickly, then use their comments to improve section labels, content order, and readability.



### Improved Wireframe

```text
+--------------------------------------+
| NAV: About | Skills | Projects |      |
|      Contact                          |
+--------------------------------------+
| Jordan                                |
| Student Portfolio                     |
| [ Toggle Dark Mode ]                  |
+--------------------------------------+
| ABOUT ME                              |
| Short introduction                    |
+--------------------------------------+
| EDUCATION                             |
+--------------------------------------+
| SKILLS                                |
+--------------------------------------+
| PROJECTS                              |
+--------------------------------------+
| CONTACT                               |
+--------------------------------------+
| FOOTER                                |
+--------------------------------------+
```

Improvement: The navigation links let an interviewer jump directly to important sections instead of scrolling through the whole page.



# Q6 screenshots

![alt text](<Screenshot 2026-08-26 at 10.19.16 PM.png>) ![alt text](<Screenshot 2026-08-26 at 10.26.49 PM.png>) ![alt text](<Screenshot 2026-08-26 at 10.27.27 PM.png>)



