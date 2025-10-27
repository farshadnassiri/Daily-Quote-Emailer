# 📧 Daily Quote Emailer 📬

A Python application that automatically sends inspirational quotes to your inbox! Start your day with motivation and inspiration! 🌟

---

## ✨ Features

- 📝 **Random Quote Selection** - Get a different inspirational quote each time
- 🎯 **Easy Configuration** - Simple environment variable setup
- 🚀 **Quick to Deploy** - Fast and straightforward implementation
- 📨 **Email Integration** - Seamless Gmail SMTP integration
- 💪 **Motivational Quotes** - Inspiring quotes from famous personalities
- 🔐 **Secure** - Uses environment variables for credentials

---

## 🎯 What Does This Do?

This project sends you daily inspirational quotes via email! It's perfect for:
- ☕ Starting your mornings with motivation
- 💡 Getting daily wisdom from great minds
- 📈 Staying inspired throughout the day
- 🎁 Sending quotes to loved ones

---

## 📋 Prerequisites

Before you begin, make sure you have:

- 🐍 **Python 3.6+** installed on your system
- 📧 A **Gmail account** with app passwords enabled
- 🌐 **Internet connection** (to send emails)

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd Daily\ Quote\ Emailer
```

### 2️⃣ Configure Your Email

You need to set up Gmail app password:

1. Go to [Google Account Settings](https://myaccount.google.com/) 👤
2. Navigate to **Security** 🔒
3. Enable **2-Step Verification** ✌️
4. Go to **App Passwords** and create one for "Mail" 📬
5. Copy the generated password 🔑

### 3️⃣ Add Your Credentials

Edit the `main.py` file and add your credentials:

```python
os.environ["mailpassword"] = "your-app-password-here"
os.environ["mail"] = "your-email@gmail.com"
```

**⚠️ Important:** Never commit your actual password to version control! Use environment variables or a `.env` file in production.

---

## 💻 Usage

### Basic Usage

Run the script:

```bash
python src/main.py
```

That's it! Your quote will be sent! 🎉

### Custom Recipients

Edit the recipient in `main.py`:

```python
send_email("Recipient Name", "recipient@email.com")
```

---

## 📁 Project Structure

```
📂 Daily Quote Emailer/
│
├── 📁 src/
│   ├── 📄 main.py        # Main application code
│   └── 📄 test.ipynb     # Testing notebook
│
├── 📄 README.md          # This file 📖
└── 📄 requirements.txt   # Python dependencies (optional)
```

---

## 🎨 Customization

### Adding More Quotes 📝

Edit the `quotes` list in `main.py`:

```python
quotes = [
    "Your quote here – Author Name",
    "Another awesome quote – Another Author",
    # Add as many as you like! 🌈
]
```

### Changing Email Subject 📧

```python
subject = "Your Custom Subject Here!"
```

### Customizing Email Body 💌

```python
body = f"Hello {recipient_name}, your custom message!\n\n{quote}"
```

---

## 🔧 Technical Details

### Dependencies

The project uses Python's built-in libraries:

- `smtplib` - For sending emails 📨
- `email` - For email formatting 📧
- `os` - For environment variables 🔐
- `random` - For quote selection 🎲

### How It Works

1. **Import libraries** 📚 - Load necessary Python modules
2. **Load quotes** 📖 - Randomly select a quote from the collection
3. **Create email** ✉️ - Format the email with recipient info
4. **Connect to Gmail** 🌐 - Establish SMTP connection
5. **Send email** 🚀 - Deliver the inspirational quote
6. **Confirmation** ✅ - Print success message

---

## 🛠️ Troubleshooting

### Issue: "Authentication failed" ❌

**Solution:** 
- Make sure you're using an app password, not your regular Gmail password 🔑
- Verify that 2-Step Verification is enabled on your Google account

### Issue: "Connection refused" 🌐

**Solution:**
- Check your internet connection 📡
- Ensure firewall isn't blocking port 587 🔥
- Verify Gmail SMTP settings

### Issue: "Module not found" 📦

**Solution:**
```bash
pip install --upgrade python
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 📜 License

This project is open source and available for educational purposes. 📚

---

## 🙏 Acknowledgments

- 💡 Inspirational quotes from great minds
- 📧 Gmail SMTP service
- 🐍 Python community
- ⭐ You for checking out this project!

---

## 📊 Future Enhancements

Potential features to add:

- ⏰ Automatic scheduling (cron jobs or task scheduler)
- 📅 Calendar integration
- 🎨 HTML email templates
- 📊 Quote analytics
- 👥 Multi-recipient support
- 🌍 Internationalization
- 🎭 Different quote categories

---

## 📞 Contact

Have questions or suggestions? Feel free to reach out!

- 📧 Email: farshadnassiri@gmail.com
- 💬 Open an issue on GitHub

---

## ⭐ Show Your Support

If you found this project helpful, consider giving it a star! ⭐

---

Made with ❤️ and Python 🐍

**Happy Coding! 🚀**

