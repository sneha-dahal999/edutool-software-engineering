# Test Cases

| ID | Requirement | Scenario | Expected result | Type |
|---|---|---|---|---|
| TC01 | FR1 | Register valid user | Account created | Functional |
| TC02 | FR1/NFR1 | Wrong password | Access denied safely | Functional/security |
| TC03 | FR2 | Exact title search | Matching book shown | Black-box |
| TC04 | FR4 | Natural-language query | Useful matches shown | Black-box |
| TC05 | FR4 | Empty query | Input handled safely | Negative/equivalence |
| TC06 | FR5 | Supported image upload | Text extracted | Functional |
| TC07 | FR3/NFR1 | User attempts admin action | Action blocked | Security |
| TC08 | FR7 | Open recommendations | Suggestions displayed | System |
| TC09 | FR2/FR4 | Complete search flow | Components return results | Integration |
| TC10 | NFR2 | Desktop/mobile screens | Content remains usable | UI |
| TC11 | Core | Repeat after fix | Old behaviour remains | Regression |
| TC12 | Core | User completes login/search | Tasks completed | Acceptance |

**Status:** Planned. No pass/fail result is claimed until the team executes and records each test.
