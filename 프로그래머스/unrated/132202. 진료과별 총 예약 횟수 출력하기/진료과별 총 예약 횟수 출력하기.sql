-- 코드를 입력하세

SELECT mcdp_cd as "진료과 코드",count(mcdp_cd) as "5월예약건" from APPOINTMENT group by mcdp_cd,to_char(apnt_ymd,'MM') having to_char(apnt_ymd,'MM') in ('05') order by count(mcdp_cd),mcdp_cd