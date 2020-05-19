from email_func import get_file_content, create_message, send_email, get_configurations


if __name__ == "__main__":
    config = get_configurations()
    sent_from = config['DEFAULT']['username']
    to = ['test1@example.com', 'test2@example.com']  
    subject = 'Testing email'  

    text = get_file_content("email.txt").decode('utf-8')
    html = get_file_content("email.html").decode('utf-8')

    msg = create_message(subject, sent_from, to, text, html)

    send_email(sent_from, to, msg)
