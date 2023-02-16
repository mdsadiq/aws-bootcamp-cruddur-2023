# Week 0 — Billing and Architecture

- listened to the discussion by chris and margaret, very useful analogies and topics
- Interesting points that should be incorporated in Software development World, not just in architecting - Iron Triangle, ask the dumb questions, rephrase the question mutiple times, be-the-packet, Requirements Risks Assumptions Constraints
- well-architected framework aws with various pillars

- setting up billing alarms and budget from console

## notes
- cloud watch has all billing data in N Virginia only.
- 10 billing alarms free in free tier
- use `gp env` instead of `export` to make the variables persist across dev environment. `gp`-> gitpod
- create accesskey  [from securuty tab in user]
- test aws connection with aws sts get-caller-identity 


- updated admin user group with billing policy

- instead of aws configure - set accesskey in environment variable - due to the way gitpod is setup.

- in  _budget.json_ file removing time period sets the time to start of the period.
- in _budget-notification-with-subscribers.json_ file replaced the email to {{youremail@email.com}} after creating budget, for privacy reasons
- In our case,i have removed the `TimePeriod` & set `TimeUnit` as  monthly will set time period ot beginning to end of the month.

-  now i have 2 budgets.

