You will be given a fee structure source (image / scanned image / PDF / screenshot / table / text).
Your task is to read the source fully, extract every visible fee component, and generate ONE SINGLE CONSOLIDATED TABLE.


1. Mandatory Source Reading

Read the image/text completely.


Extract every fee component shown.


Do not skip any fee, even small ones (sports, establishment, association, insurance, digital activity, etc.).


Do not hallucinate fees or amounts.


If a fee or its frequency is unclear → treat it as not provided and exclude.



2. Output Structure (NON-NEGOTIABLE)

Always output ONE SINGLE TABLE


❌ Never create multiple tables


❌ Never split output by course, quota, or year


Final table columns must be exactly:
| Course Name | Quota | Year / Semester | Tuition Fee (₹) | Other Fees (JSON) | Total Fee (₹) |
Each row represents one unique combination of:


Course (with specialization if applicable)


Quota


Year or Semester



3. Course Naming Convention (STRICT & LOCKED)
You must only modify names using the following patterns.

Do not invent styles or formats outside these.

UG / PG / Integrated / Doctoral Naming

Bachelor of Architecture

Bachelor of Architecture [B.Arch] (Specialization if given)


Bachelor of Planning

Bachelor of Planning


Integrated Science Programme

Bachelor of Science [B.Sc] + Master of Science [M.Sc] (Specialization)


Bachelor of Technology

Bachelor of Technology [B.Tech] (Specialization)


Bachelor of Technology – Lateral Entry

Bachelor of Technology [B.Tech] {Lateral} (Specialization)


Master of Business Administration

Master of Business Administration [MBA] (Specialization if given)


Master of Computer Applications

Master of Computer Applications [M.C.A] (Specialization if given)


Master of Planning

Master of Planning [M.Plan]


Master of Technology

Master of Technology [M.Tech] (Specialization)


Doctoral Programme

Ph.D. (Specialization)


General Rule

Expand abbreviations correctly

(e.g., AI → Artificial Intelligence, E&I → Electronics and Instrumentation Engineering)


If specialization is not given, do not add one


Never group multiple specializations under one course name



4. Semester vs Year Rule (CRITICAL)

If the source is semester-wise → output semester-wise


If the source is year-wise → output year-wise


❌ Never convert semester fees into yearly or vice-versa unless explicitly instructed



5. “1st Year Fees” Interpretation Rule

If the source says “fees for 1st year students”:


Treat the fee as applicable to all academic years


Replicate the same fee for remaining years unless explicitly stated otherwise




6. Fee Placement Rules

If NO breakup of other fees is given:


Place the entire amount in Tuition Fee (₹)


Other Fees (JSON) must be []



If breakup IS given:


Tuition → Tuition Fee column only


All other components → JSON




7. Fee Classification

Tuition Fee → ONLY in Tuition Fee column


One-time fees (admission, registration, matriculation, caution):


Appear only in first applicable row


Must be 0 later



Recurring fees:


Appear only in the exact semesters/years shown


❌ Do not auto-repeat unless shown in source



Optional/conditional fees → exclude unless mandatory for all



8. Refund Rules

"refund":"1" → only if explicitly refundable


"refund":"0" → default


❌ No refund field allowed for:


admission_fee


registration_fee


exam_fee




9. Quota Handling

Each quota → separate rows in the same table


❌ Never merge quotas


❌ Never assume quota differences


Special NRI Rule

If NRI fees are in USD / foreign currency:


STOP


Ask user:

“Please provide the current USD → INR exchange rate to be used.”


Generate output only after rate is provided


Row order:


General quota first


NRI quota next (converted using user-given rate)




❌ Never assume exchange rates



10. JSON Rules (Very Strict)

Flat array only


One object = one fee


Include fee even if value is "0"


Numeric values → strings without commas


No nesting, no grouping



11. Total Calculation — ZERO-ERROR RULE
Before output:


Sum all JSON values numerically


Add Tuition Fee


Re-check arithmetic manually


If image shows total → must match exactly


❌ Incorrect totals are not allowed


12. Hard Constraints

❌ No hallucination


❌ No skipped fees


❌ No wrong totals


❌ No grouping of courses


❌ No multiple tables


✅ Always one consolidated table


✅ Naming convention must be followed exactly
