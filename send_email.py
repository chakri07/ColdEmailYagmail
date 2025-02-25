import yagmail
import os

def send_recruiter_email_yagmail(sender_email, sender_password, recipient_emails, subject, body, attachment_path=None):
    """Sends a standard email template with an optional attachment to a list of recruiter emails using yagmail."""

    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        for recipient_email in recipient_emails:
            contents = [
                f"""Dear Recruiter,\n\n{body}\n\nSincerely,\n\n[Your Name]\n[Your Phone Number]\n[Your LinkedIn Profile URL (Optional)]""",
                f"""<html><body><p>Dear Recruiter,<br><br>{body}<br><br>Sincerely,<br><br>[Your Name]<br>[Your Phone Number]<br><a href="[Your LinkedIn Profile URL (Optional)]">LinkedIn Profile</a></p></body></html>"""
            ]

            if attachment_path:
                yag.send(to=recipient_email, subject=subject, contents=contents, attachments=attachment_path)
            else:
                yag.send(to=recipient_email, subject=subject, contents=contents)

            print(f"Email sent successfully to {recipient_email}")
        yag.close()
    except Exception as e:
        print(f"Failed to send emails. Error: {e}")



# Example usage:
sender_email = os.getenv("EMAIL_USERNAME")+ "@gmail.com"
sender_password = os.getenv("EMAIL_PASSWORD")


print(os.getenv('super_secret'))
print(os.getenv('user_name'))
recipient_emails = ["chakrispam@gmail.com"]
subject = "Application for [Job Title]"
body = """I am writing to express my interest in [Job Title] position. I have [Number] years of experience in [Relevant Field] and possess the skills and qualifications outlined in the job description. I am particularly interested in [Specific Aspect of the Company or Role]. I have attached my resume for your review and would welcome the opportunity to discuss my qualifications further."""
attachment_path = "./chakradhar_gummidela.pdf"  # Replace with the actual path to your resume. If you don't want to attach anything, set this to None.

send_recruiter_email_yagmail(sender_email, sender_password, recipient_emails, subject, body, attachment_path)