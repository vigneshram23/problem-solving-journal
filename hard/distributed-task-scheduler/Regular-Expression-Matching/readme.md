10. Regular Expression Matching
📌 Problem Overview
This problem implements a simplified regular expression engine that supports:
. → Matches any single character
* → Matches zero or more occurrences of the preceding character
The goal is to check whether the entire input string matches the pattern — partial matches are not allowed.
This is a classic problem that tests string processing, dynamic programming, and pattern parsing skills.

🧠 Why This Problem Matters
Although the problem looks academic, it models the core mechanics of real-world regex engines and appears in multiple production systems.
Understanding this problem builds foundational skills used in:
Input validation engines
Log processing systems
Query parsing and filtering
Rule-based matching systems
Compilers and interpreters

## 🌍 Real-World Use Cases
1️⃣ Input Validation Systems
Used to validate:
Email formats
Phone numbers
Usernames and passwords
Form inputs in web applications
Example:
Pattern: a*b
Input: aaab  → Valid

2️⃣ Log Filtering & Monitoring (DevOps / SRE)
Log aggregation tools use regex-style matching to:
Detect errors
Filter events
Trigger alerts
Example:
Pattern: ERROR.*
Log: ERROR connection failed

3️⃣ Search Engines & Query Parsing
Search engines use pattern matching to:
Interpret wildcard queries
Match flexible search conditions
Example:
Pattern: doc.*2024
Matches: document_2024.pdf

4️⃣ Security Systems (WAF / IDS)
Web Application Firewalls (WAF) use pattern matching to:
Detect malicious payloads
Identify injection patterns
Block suspicious inputs
Example:
Pattern: .*<script>.*

5️⃣ Compiler Design & Language Parsers
Compilers use regex engines to:
Tokenize source code
Identify keywords and literals
Perform lexical analysis
This problem mirrors finite automata-based matching logic used in compilers.

6️⃣ AI / NLP Pre-Processing Pipelines
Before text reaches ML models, regex is used for:
Cleaning text
Normalizing patterns
Filtering noisy inputs

## 💡 Solution Strategy
We use bottom-up Dynamic Programming to check whether prefixes of the string match prefixes of the pattern.

## 🧩 Dynamic Programming Definition
dp[i][j] = True if s[0:i] matches p[0:j]

Where:
i = length of string prefix
j = length of pattern prefix

## 🧠 Core Matching Rules
1️⃣ Direct Match or Wildcard .
If:
p[j-1] == s[i-1] OR p[j-1] == '.'

Then:
dp[i][j] = dp[i-1][j-1]

2️⃣ Handling *
* applies to the preceding element.
Two possibilities:
Zero occurrences
dp[i][j] = dp[i][j-2]

One or more occurrences
If preceding character matches:
dp[i][j] |= dp[i-1][j]

## 🧪 Sample Test Cases
assert Solution().isMatch("aa", "a") == False
assert Solution().isMatch("aa", "a*") == True
assert Solution().isMatch("ab", ".*") == True
assert Solution().isMatch("aab", "c*a*b") == True
assert Solution().isMatch("mississippi", "mis*is*p*.") == False

## ⏱️ Performance Analysis
Metric
Value
Time Complexity
O(m × n)
Space Complexity
O(m × n)
Max Constraints
m, n ≤ 20


## ⚡ Alternative Approach (Mentioned for Completeness)
A recursive backtracking + memoization solution can be faster in practice due to early pruning.
However:
Harder to reason about
Requires careful base-case handling
Recursion depth risk in Python
For clarity and reliability, this repository uses bottom-up DP.

## 🎯 Interview Value
This problem demonstrates:
Dynamic Programming mastery
Pattern matching logic
Edge case handling
Engineering trade-offs (clarity vs performance)
Interviewers often use this problem to test deep reasoning, not syntax.