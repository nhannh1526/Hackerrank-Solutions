/*
 Enter your query here.
 */
SELECT COMPANY.COMPANY_CODE,
       COMPANY.FOUNDER,
       COUNT(DISTINCT LEAD_MANAGER.LEAD_MANAGER_CODE),
       COUNT(DISTINCT SENIOR_MANAGER.SENIOR_MANAGER_CODE),
       COUNT(DISTINCT MANAGER.MANAGER_CODE),
       COUNT(DISTINCT EMPLOYEE.EMPLOYEE_CODE)
FROM COMPANY
         INNER JOIN LEAD_MANAGER ON COMPANY.COMPANY_CODE = LEAD_MANAGER.COMPANY_CODE
         INNER JOIN SENIOR_MANAGER ON LEAD_MANAGER.LEAD_MANAGER_CODE = SENIOR_MANAGER.LEAD_MANAGER_CODE
         INNER JOIN MANAGER ON SENIOR_MANAGER.SENIOR_MANAGER_CODE = MANAGER.SENIOR_MANAGER_CODE
         INNER JOIN EMPLOYEE ON MANAGER.MANAGER_CODE = EMPLOYEE.MANAGER_CODE
GROUP BY COMPANY.COMPANY_CODE,
         COMPANY.FOUNDER
ORDER BY COMPANY.COMPANY_CODE