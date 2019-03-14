# pwnd-password-check

Checks if your password was found in haveibeenpwned.com's Database.
This script creates a sha1 hash of your password and then sends the first 5 characters to 
haveibeenpwned.com's REST Api. After this it looks for your hash in the response.
With this method, your password wont be sent anywhere.

## Getting Started

```
python main.py <password>
```
If your password has spaces use:
```
python main.py "<password>"
```

### Prerequisites

python3

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details