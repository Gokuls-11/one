
PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> git credential-manager erase

fatal: Missing 'protocol' input argument
PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> git credential-manager erase
protocol=https
host=github.com

PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> git push -u origin main     
remote: Permission to Gokuls-11/one.git denied to Gokuls-11.
fatal: unable to access 'https://github.com/Gokuls-11/one.git/': The requested URL returned error: 403
PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> git remote remove origin
PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> git remote add origin https://github.com/Gokuls-11/one.git
PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 2.03 KiB | 2.03 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Gokuls-11/one.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\nvgok\OneDrive - SSN-Institute\Academics\sem4\software\testpractice> 
