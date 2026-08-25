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


