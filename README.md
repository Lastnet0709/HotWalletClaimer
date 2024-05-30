# Telegram Claim Assistant - Mine HOT & More!

Hello, Fellow Crypto Game Enthusiasts! To keep up with the latest updates and changes, check out our change log on [Patreon](https://www.patreon.com/TelegramClaimBot)—it's free to read! If you find the scripts useful and would like to support our ongoing development, consider subscribing to our Patreon, or treat us to a [cup of coffee](https://www.buymeacoffee.com/HotWallletBot) ☕ as a token of appreciation - both are just $5. You can also support us at no cost by subscribing to and watching our [YouTube channel](https://www.youtube.com/channel/UCygSGwCLIaQAZiYs1lLcRGw), where we share more content and insights. You can even see some humorous uses for the channel and more reasons to give a little back [here](docs/YOUTUBE.md).

## Clever Claiming - How to Use a Virtual Browser and Python Script to Maximize Rewards 24/7

Many popular Telegram apps require frequent logins to maximize rewards. This Python script utilizes Selenium and a virtual web browser to mimic human-like interaction with the games without using programmatically triggered API calls, which might arouse suspicion. Designed to run on your local computer or VPS, it automates the claim process by monitoring your account status within the app and claiming rewards at the most opportune moments. It operates fully automatically when properly configured, with an optional random timer offset to further emulate human behavior.

For example, consider the cryptocurrency "HOT" on the Near Protocol. Mining occurs through the "@HereWalletBot" - a Telegram-based, Web3-enabled app on the NEAR Protocol blockchain. To maximize rewards, users must regularly visit to claim tokens. This script tracks the time until the storage pot fills and initiates a claim when it's full. If the storage is not full, it calculates the time until completion and waits for the optimal moment—adjusted by your preferred random offset—to claim, thereby minimizing network load and reducing gas fees.

Similarly, you can automate interactions with "Ocean" on SUI, "Vertus" on TON, "Oxygen" on Polygon, and both "Cold" and "Tree" on BSC using their respective Telegram bots. Each bot allows users to claim tokens and manage their rewards efficiently by automating the timing of claims, ensuring that you maximize your mining potential while minimizing transaction costs. The script also supports "Seed," which is not associated with a specific blockchain but still offers reward opportunities through automated claims.

We aim to expand this script to include other projects suggested by our users in the coming weeks and months. However, we do not endorse any projects, some of which may take time and effort to mine but ultimately might yield little to no real-world value and may try to upsell additional features or incur gas fees. As always, doing your own research is essential in cryptocurrency.

## 🎥 Step-by-Step Video Walkthrough 🎬

Watch along while I perform each step, from server setup, downloading and installing the script, configuring the options, and initiating your automated claims with the [Video Walkthrough](#videos).

## Quick Start Install via Docker (best option for non-technical users)

Using Docker simplifies the setup for non-technical users, by "containerizing" the application and its dependencies, keeping it separate from your main operating system, and ensuring a consistent environment across different architectures (X86/ARM64) and operating systems (Linux-based/Windows). This approach eliminates issues related to dependency management and version conflicts.

Install Docker Desktop on your PC or CLI Docker on a VPS and then type the following commands into a terminal. Refer to the [DOCKER.md](docs/DOCKER.md) or video walkthrough for full details.

#### To Set Up a Container with the Script and Dependencies from the Latest Image
```sh
docker run -d --name telegram-claim-bot --restart unless-stopped thebrumby/telegram-claim-bot
```
With this command, the container will run in the background even when you are not interacting with it. If your machine restarts, the container will automatically restart the script with Docker.
#### To Interact with the Script, Including Adding New Game Accounts or Monitoring for Errors
```sh
docker exec -it telegram-claim-bot /bin/bash
```
#### Some Examples to Add a Game or Remove a Game
```sh
# To add a game:
./launch.sh
# To remove a no longer wanted, or corrupted game:
./remove-process.sh
# Predefining the game name and your wallet name:
./launch.sh cold BNB-Cold:Wallet1
# Advanced example - specifying the seed phrase in the command line only works with HOT so far:
./launch.sh hot HOT:Wallet1 --seed-phrase wordone wordtwo wordthree wordfour wordfive wordsix wordseven wordeight wordnine wordten wordeleven wordtwelve
```
#### To return to the command-line interface type "exit or press ctrl+d
```sh
exit
```
#### Stop the System from Auto-Updating from GitHub

By default, the system will pull any changes from GitHub twice a day and restart any affected running scripts with the latest code. You can stop this with the following command, but only **AFTER** you have another process (e.g., a game) running in PM2:

```sh
pm2 stop daily-update
```

## Windows 10 & 11 Alternative Installation - Utilize WSL2:
You can check out the [WINDOWS.md](docs/WINDOWS.md) guide or checkout this [video](https://www.youtube.com/watch?v=wOajWwO32P4) for further instructions.

<a name="quick-start"></a>
## Stand-alone Linux Installation (best option for technically-minded users):
To create a stand-alone (non-Docker) version, follow the instructions at [LINUX.md](docs/LINUX.md) or watch the [video](https://www.youtube.com/watch?v=aXwg8U4Qlvc) walkthrough. This method is compatible with Ubuntu-style operating systems and tested on Ubuntu 20.04 - 24.04. 

## Games/apps currently working with this script:
**Note: All these scripts assume you have already manually started your selected game, completed any one-time screens that require reading, and made at least 1 claim manually - ensuring you have coins for Gas Fee if necessary**

| Command                       | Mining Game Link in Telegram                    | Ubuntu | Docker |
|-------------------------------|-------------------------------------------------|--------|--------|
| `./launch.sh hot`             | Launch HOT on Near Protocol: [@herewalletbot](https://t.me/herewalletbot) | ✅     | ✅     |
| `./launch.sh cold`            | Launch Cold on BNB Wallet: [@Newcoldwallet_bot](https://t.me/Newcoldwallet_bot) | ✅     | ✅     |
| `./launch.sh vertus`          | Launch Vertus on TON: [@Vertus_App_bot](https://t.me/vertus_app_bot) | ✅     | ✅     |
| `./launch.sh tree`            | Launch Tree on BNB Wallet: [@treeminebot](https://t.me/treeminebot/app?startapp=6783218884) | ✅     | ✅     |
| `./launch.sh wave`            | Launch Wave Wallet on Sui: [@waveonsuibot](https://t.me/waveonsuibot/walletapp?startapp=1809774) | ✅     | ✅     |
| `./launch.sh seed`            | Launch Seed App - Mine Seed: [@seed_coin_bot](https://web.telegram.org/k/#@seed_coin_bot) | ✅     | ✅     |
| `./launch.sh blum`            | Mine Blum: [@BlumCryptoBot](https://web.telegram.org/k/#@BlumCryptoBot) | ❌     | ❌     |
| `./launch.sh oxygen`            | Mine Blum: [@oxygenminerbot](https://web.telegram.org/k/#@oxygenminerbot) | ✅     | ✅     |

💻 **TIP:** Each session while in wait status uses around 30mb of memory and virtually no CPU load. During the Claim or Login phases, however, each session requires approximately 450 MB of memory and utilizes a larger portion of your CPU resources. The concurrent claims setting (default value 1) limits the number of active claims to prevent hardware overload. Assess your hardware's capacity to determine how many simultaneous sessions it can handle, and adjust the maximum number accordingly by following the [Usage Notes](#usage-notes). Even with a maximum of one allowed claim session, claiming on multiple wallets is easily possible; additional claims just queue until a claim session slot becomes available.
<a name="videos"></a>
| Step-by-Step Video Walkthrough                                                                                                   | YouTube Link                                                                                                                                                                                                                                     | Video Length |
|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| **Introduction: Play2Earn - Automating Claims in Telegram Games with Python - Hot, Cold, Vertus, and Tree**  
Dive into the exciting world of Play2Earn games as we explore automation techniques using Python. This video provides a comprehensive walkthrough on how to set up automated claims for games such as Hot, Cold, Vertus, and Tree. Learn how to efficiently manage game rewards and maximize your earnings with our step-by-step guide.       | [![Play2Earn: Automating Claims in Telegram Games with Python - Hot, Cold, Vertus, and Tree](https://img.youtube.com/vi/cub6cIg6d1o/0.jpg)](https://www.youtube.com/watch?v=cub6cIg6d1o)<br>[Watch Video](https://www.youtube.com/watch?v=cub6cIg6d1o)    | 03:38        |
| **Windows Guide: Experience the Simplicity of Docker**  
Explore how to use Docker, a powerful tool for rolling out software such as our automation script. This guide is tailored for Windows users, providing a straightforward approach to setting up and using Docker for efficient software deployment. | [![Windows Guide: Experience the Simplicity of Docker](https://img.youtube.com/vi/5lwO3KogPnQ/0.jpg)](https://www.youtube.com/watch?v=5lwO3KogPnQ)<br>[Watch Video](https://www.youtube.com/watch?v=5lwO3KogPnQ) | 10:09        |
| **Step 2a: Setting Up an Amazon VPS for Automated Crypto Claiming Scripts**  
Setting up a virtual private server (VPS) on Amazon Web Services is easier than you think! This tutorial covers everything from creating your VPS to configuring it for automated crypto claiming scripts. Whether you're managing Hot, Cold, Vertus, or Tree, these strategies will help streamline your operations and enhance your mining efficiency.      | [![Setting Up an Amazon VPS for Automated Crypto Claiming Scripts](https://img.youtube.com/vi/aXwg8U4Qlvc/0.jpg)](https://www.youtube.com/watch?v=aXwg8U4Qlvc)<br>[Watch Video](https://www.youtube.com/watch?v=aXwg8U4Qlvc)                            | 03:57        |
| **Step 2b: Setting Up Ubuntu on Windows Using WSL for Crypto Automation**  
Learn how to integrate Ubuntu with Windows using the Windows Subsystem for Linux (WSL) for enhanced crypto automation capabilities. This guide will take you through the installation and setup process, showing you how to prepare your system for automating claims in games like Hot, Cold, Vertus, and Tree.       | [![Setting Up Ubuntu on Windows Using WSL for Crypto Automation](https://img.youtube.com/vi/wOajWwO32P4/0.jpg)](https://www.youtube.com/watch?v=wOajWwO32P4)<br>[Watch Video](https://www.youtube.com/watch?v=wOajWwO32P4)                               | 03:47        |
| **Step 3: Installing the Python Script and Configuring Automated Claims**  
Master the setup of automated claiming scripts in this detailed tutorial. We walk you through the installation of necessary Python scripts and show you how to configure them for efficient operation across various games such as Hot, Cold, Vertus, and Tree. This video is perfect for anyone looking to automate their gameplay and claiming process.       | [![Installing the Python Script and Configuring Automated Claims](https://img.youtube.com/vi/Wg2gQBrlCIc/0.jpg)](https://www.youtube.com/watch?v=Wg2gQBrlCIc)<br>[Watch Video](https://www.youtube.com/watch?v=Wg2gQBrlCIc)                             | 06:37        |
| **Step 4: Setting Up Telegram Accounts: QR Codes and One-Time Passwords**  
Setting up Telegram accounts for mining games doesn't have to be complex. This guide demonstrates the use of QR codes and one-time passwords to access games like Hot, Cold, Vertus, and Tree. Follow along to learn how to secure and optimize your game accounts for maximum productivity and ease of use.       | [![Setting Up Telegram Accounts: QR Codes and One-Time Passwords](https://img.youtube.com/vi/gYeiWolV6oY/0.jpg)](https://www.youtube.com/watch?v=gYeiWolV6oY)<br>[Watch Video](https://www.youtube.com/watch?v=gYeiWolV6oY)                          | 03:45        |
| **Mining Hot on Near Protocol - Wallet Setup and Automated Claiming Guide**  
This tutorial focuses on setting up a wallet and automating claims for the Hot game on the Near Protocol blockchain. We'll show you the crucial steps to ensure your wallet is properly configured and automated to claim rewards efficiently. Whether you're a beginner or an experienced miner, these insights will help you make the most of your mining efforts.       | [![Mining Hot on Near Protocol - Wallet Setup and Automated Claiming Guide](https://img.youtube.com/vi/hLBeF4o65KI/0.jpg)](https://www.youtube.com/watch?v=hLBeF4o65KI)<br>[Watch Video](https://www.youtube.com/watch?v=hLBeF4o65KI)                    | 05:42        |
| **Automating Tree Mining with BNB Wallet: Setup and Claims Guide**  
Automate your Tree mining efforts using the BNB Wallet with this straightforward guide. Discover the essential steps for setting up your wallet, initiating claims, and optimizing the process to ensure continuous mining success. This video will equip you with the tools and knowledge needed to effectively manage and automate your mining operations.       | [![Automating Tree Mining with BNB Wallet: Setup and Claims Guide](https://img.youtube.com/vi/YQBemSH3uOA/0.jpg)](https://www.youtube.com/watch?v=YQBemSH3uOA)<br>[Watch Video](https://www.youtube.com/watch?v=YQBemSH3uOA)                            | 03:04        |

<a name="pm2"></a>
### Addional Process Manager 2 ```PM2``` commands you may find useful.  

- View all PM2 managed processes:
    ```bash
    pm2 list
    ```
- View logs for a specific session (Replace `HOT:Wallet1` with the actual name):
    ```bash
    pm2 log HOT:Wallet1
    ```
- To remove a managed wallet:
    ```bash
    pm2 delete HOT:Wallet1
    ```
- Save configuration if you add or delete processes:
    ```bash
    pm2 save
    ```

<a name="usage-notes"></a>
## V3.0.3 Release Notes. 

## Usage Instructions
After executing the script with ```./launch.sh```, you will be prompted to update settings and configure the session:

### Update Settings
   - If you choose "yes" to update settings when prompted, you can review and possibly update the following settings:
      - `forceClaim`: Choose to force a claim the first time the script runs, regardless of whether the wallet is full.
      - `debugIsOn`: Activate debugging to save screenshots locally; default is off.
      - `hideSensitiveInput`: Ensures sensitive information like phone numbers and seed phrases remain hidden; default is ON.
      - `screenshotQRCode`: Prefer to log in via QR code; the alternative is manual login via phone number and OTP.
      - `maxSessions`: Set the maximum number of concurrent claim sessions; additional wallets will wait for an available slot.
      - `verboseLevel`: Adjust the verbosity of console messages; options range from 1 (minimal) to 3 (all messages).
      - `forceNewSession`: Forces a new login, useful if the existing session encounters errors.
      - `lowestClaimOffset` and `highestClaimOffset`: Define the range for randomized claim timing relative to when the pot is filled.
         - **Examples of Random Claim Timing based on Claim Offset:**
            - `-30, -15`: Early claims randomly between 30 and 15 minutes before the pot is full.
            - `30, 60`: Late claims randomly 30 minutes to 1 hour after the pot is full.
            - `-15, 15`: Random claims within a 15-minute window either side of the pot being filled.

### Session Name Configuration
   - Sessions are auto-named numerically in the format "Wallet1", or can be customized to your own choice. Reusing a name attempts to resume that session.

### Telegram Login: Saved Account Options
   - If the script detects you have a saved Telegram session, you can choose it from a numbered list. 
   - If you prefer to log into a new account, selecting 'n' proceeds to a new Telegram login. The default method is to log in by scanning a QR Code screenshot.
   - Should the QR Code method be unsuccessful, or if you disable it in settings, follow the OTP login procedure outlined below.

### Telegram OTP login: Country Name and Phone Number for Telegram
   - Enter your Country Name as displayed on Telegram's login page or accept the default, which is auto-detected based on your IP.

### Telegram OTO login: One-Time Password (OTP)
   - Enter the OTP sent to your registered Telegram account.

### Telegram login: Two-factor authentication (2FA)
   - If 2FA is enabled on your Telegram account, enter your 2FA password following the QR code scan or OTP entry.

### Game login: Seed Phrase Input for HereWalletBot Login
   - If your selected game requires a seed phrase to log in, carefully input your 12-word seed phrase, ensuring correct spacing without any punctuation or numbers.
   - Alternatively, if the game's login is based on the Telegram account, ensure you are logging into the correct account.

### Final options once the PM2 session is configured.
   - Select "a" or press <enter> to automatically add the session to PM2.
   - Select "e" to exit to the Command Line Interface without adding to PM2
   - Select "y" to continue and attempt to make a claim. 

Remember to check and adjust your settings upon startup to optimize the script's performance to your server's capabilities.

After following these steps, if all inputs are correctly entered, and assuming no flooding block is in place, you'll be successfully logged into Telegram and your chosen game.

# Security Considerations for HotWalletClaimer Usage

💡 Communication: The only external communication is with the Telegram Web App, which occurs over HTTPS, providing a secure channel.

⚠️ Your seed phrase and Telegram login details are not stored or transmitted by this script, except during the unavoidable one-time login process. As of version v1.3.4, the Google Chrome session is now saved into the ```selenium``` folder, as of v.1.3.6 there is also a duplicate of the session in ```./HotWalletBot/backups``` - if this information were to become compromised, it would allow a suitably experienced individual to access your account.  

💡 Debugging: Enabling debug mode captures the whole process as screenshots, excluding the seed phrase entry step. These images are stored locally to assist you in the event of errors and are not otherwise transmitted or uploaded in any way.

## Security Best Practice:

💡 Private Devices: Only use this script on private, secure machines or Virtual Private Servers that only you can access.

⚠️ Caution with Seed Phrases: Be very cautious with accounts of significant value. Consider the effect of any unintended loss should your seed phrase become compromised.

💡 Awareness and Discretion: Understand the security trade-offs of using this automation tool or any other third-party tools. Your vigilance is crucial in safeguarding your information.

## Disclaimer:
Use of HotWalletClaimer is at your own risk. While we are confident that the script neither transmits nor stores your sensitive data, it is essential to acknowledge that devices can become compromised through viruses or other malicious software. The developers of HotWalletClaimer exclude any liability for potential security breaches or financial losses. It is your responsibility to safeguard your digital security. Always prioritize protecting your accounts and sensitive information.

