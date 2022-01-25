#Function: Selected Path is to be scanned and compared to the second selcected Path.
#If there are Folders not existing, the script has to copy them.

import sys
import shutil
import time
import filecmp
import os.path
import datetime
import os
import threading


def main():

    print("\r\nbackup.py is running...\r\n")

    def copytree():
        dir1 = sys.argv[3]
        dir2 = sys.argv[5]
        src = dir1
        dst = dir2
        try:
            print("This might take a long time. Be patient.")
            shutil.copytree(src, dst, dirs_exist_ok=True)

        except KeyboardInterrupt:
            print("Script shut down...")
            sys.exit()

        except shutil.Error:
            print("shutil_module_error. (probably permission denied file)                            ")
            end_check(dir1, dir2)
            sys.exit()

        except OSError:
            print("some files may be unable to copy. (crashed files)                ")
            pass

    def get_size(dir1):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(dir1):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def analyze_p(dir1, dir2):
        files1 = 0
        dirs1 = 0
        files2 = 0
        dirs2 = 0
        for base, dirs, files in os.walk(dir1):
            for directories in dirs:
                dirs1 += 1
            for Files in files:
                files1 += 1
        for base, dirs, files in os.walk(dir2):
            for directories in dirs:
                dirs2 += 1
            for Files in files:
                files2 += 1
        return files1, dirs1, files2, dirs2

    def size_def(size_src, size_dst):
        if size_src > 1024:
            # kilobyte
            size_src = size_src / 1024
            size_s = "KB"
            if size_src >= 1000:
                # megabyte
                size_src /= 1000
                size_s = "MB"
                if size_src >= 1000:
                    # gigabyte
                    size_src /= 1000
                    size_s = "GB"
                    if size_src >= 1000:
                        # terabyte
                        size_src /= 1000
                        size_s = "TB"
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            size_s = "byte"
        if size_dst > 1024:
            # kilobyte
            size_dst /= 1024
            size_d = "KB"
            if size_dst >= 1000:
                # megabyte
                size_dst /= 1000
                size_d = "MB"
                if size_dst >= 1000:
                    # gigabyte
                    size_dst /= 1000
                    size_d = "GB"
                    if size_dst >= 1000:
                        # terabyte
                        size_dst /= 1000
                        size_d = "TB"
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            size_d = "byte"

        return size_src, size_s, size_dst, size_d

    def r_process():
        dir1 = sys.argv[3]
        dir2 = sys.argv[5]
        finished = False
        file_d1, dirs_1, file_d2, dirs_2 = analyze_p(dir1, dir2)
        og_size_dst = get_size(dir2)
        while not finished:
            finished = compare_trees(dir1, dir2)
            file1_d1, dirs1, file2_d2, dirs2 = analyze_p(dir1, dir2)
            size_src = get_size(dir1)
            size_dst = get_size(dir2) - og_size_dst
            file2_d2 = file2_d2 - file_d2
            size_src, size_s, size_dst, size_d = size_def(size_src, size_dst)

            if not finished:
                if file1_d1 >= file2_d2:
                    print("Copy files(", file2_d2, "/", file1_d1, ")", "|", "(", "%.2f" % size_dst, size_d, "/",
                          "%.2f" % size_src, size_s, ")        ", end="\r")
                    # size_sum = size_dst / size_src
                    # size_sum *= 100
                    # time_per_sec = 130000000
                    # time_ = size_src / time_per_sec  # 305
                    # time_ = int(time_)
                    # n_time = time_ / 100
                    # for status in range(100):
                    # time.sleep(n_time)
                    # status += 1
                    # print("Copy files(", status, "%)", end="\r")

                else:
                    dot1 = ".                                   "
                    dot2 = "..                                  "
                    dot3 = "...                                 "
                    print("Copy files ", dot1, "     ", end="\r")
                    time.sleep(0.2)
                    print("Copy files ", dot2, "   ", end="\r")
                    time.sleep(0.2)
                    print("Copy files ", dot3, end="\r")

            elif finished:
                print("Copy files(", file2_d2, "/", file1_d1, ")", "|", "(", "%.2f" % size_src, size_s, "/",
                      "%.2f" % size_src, size_s, ")       ", end="\r")
                print("\r\nDone.")

            else:
                print("An error occurred.")
                sys.exit()

    def compare_trees(dir1, dir2):
        file1_d1, dirs1, file2_d2, dirs2 = analyze_p(dir1, dir2)
        size_src = get_size(dir1)
        size_dst = get_size(dir2)

        dirs_cmp = filecmp.dircmp(dir1, dir2)
        if len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or \
                len(dirs_cmp.funny_files) > 0 or file1_d1 != file2_d2 or size_src != size_dst:
            return False
        else:
            return True

    def are_dir_trees_equal(dir1, dir2):
        print("Analysing paths...")
        file1_d1, dirs1, file2_d2, dirs2 = analyze_p(dir1, dir2)
        size_src = get_size(dir1)
        size_dst = get_size(dir2)
        try:
            if not compare_trees(dir1, dir2):
                if file1_d1 == file2_d2 and size_src != size_dst:
                    print("Backup necessary.")
                    copy_files(dir1, dir2)

                elif file1_d1 != file2_d2 and size_src != size_dst:
                    print("Backup necessary.")
                    copy_files(dir1, dir2)

                else:
                    print("ERROR: Paths might be corrupted.")

            else:
                print("Paths already equal. No backup necessary.")
                sys.exit()

        except FileNotFoundError:
            print("ERROR: Selected file or directory not found.")
            sys.exit()

        except FileExistsError:
            print("ERROR: Selected file or directory doesn't exist.")
            sys.exit()

        except OSError:
            print("Some files may be unable to copy. (damaged files)")
            sys.exit()

        end_check(dir1, dir2)

    def end_check(dir1, dir2):
        print("Checking files...")
        if compare_trees(dir1, dir2):
            print("Files copied successfully.")
            sys.exit()
        else:
            print("Some files/metafiles failed to copy. Retry script, otherwise check manual if all files were copied.")
            sys.exit()

    def copy_files(dir1, dir2):
        dirs_cmp = filecmp.dircmp(dir1, dir2)
        try:
            file1_d1, dirs1, file2_d2, dirs2 = analyze_p(dir1, dir2)

            if len(dirs_cmp.left_only) == 0:
                print("No files to copy.")
                sys.exit()
            elif len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or \
                    len(dirs_cmp.funny_files) > 0 or file1_d1 != file2_d2:
                thread1 = threading.Thread(target=r_process)
                thread2 = threading.Thread(target=copytree)
                thread1.start()
                thread2.start()
                thread1.join()
                thread2.join()
            else:
                print("No backup necessary")
                sys.exit()

        except shutil.Error:
            print("shutil_module_error. (probably permission denied file)                            ")
            end_check(dir1, dir2)
            sys.exit()

        except OSError:
            print("ERROR: fatal python error.")
            sys.exit()



    #def print_files(dir1, dir2):
        #files_dir2 = os.listdir(dir2)
        #count_files_dir2 = len(files_dir2)
        #count = 0
        #if count < count_files_dir2:




    def backup():
        if len(sys.argv) == 2:
            if sys.argv[1] == "--help":
                print("""
 Usage:
        -b              # Backup mode.
        -src [INPUT]    # Path of file or directory you want to copy.
        -dst [INPUT]    # Destination path of the copy.
        
        Example: python backup.py -b -src D:/pictures -dst G:/backup 
        
        Note: - every file/directory from the selected path is copied to the destination path
                not the folder itself.
              - script works perfect by creating a new destination folder previously. 
        
                  """)
            else:
                print("ERROR. Wrong input. Try --help for usage.")
                sys.exit()
        elif len(sys.argv) == 6:
            if sys.argv[1] == "-b" and sys.argv[2] == "-src" and sys.argv[4] == "-dst":
                dir1 = sys.argv[3]
                dir2 = sys.argv[5]
                size_src = get_size(dir1)
                size_dst = get_size(dir2)
                size_src, size_s, size_dst, size_d = size_def(size_src, size_dst)
                file1_d1, dirs1, file2_d2, dirs2 = analyze_p(dir1, dir2)
                print("-" * 50)
                print("Script by John Ryder v1.0.2")
                print("Datetime: ", str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                print("Number of files", sys.argv[3], ": ",
                      file1_d1, "| (", "%.2f" % size_src, size_s, ")")
                print("Number of files", sys.argv[5], ": ",
                      file2_d2, "| (", "%.2f" % size_dst, size_d, ")")
                print("-" * 50)
                are_dir_trees_equal(dir1, dir2)
            else:
                print("ERROR. Wrong input. Try --help for usage.")
                time.sleep(2)
                sys.exit()

        else:
            print("ERROR. Wrong input. Try --help for usage.")
            time.sleep(2)
            sys.exit()

    backup()


try:
    main()

except KeyboardInterrupt:
    print("Script shut down...")
    sys.exit()
except FileNotFoundError:
    print("Some files doesn't exist.")
    pass
except FileExistsError:
    print("Some files already exist.")
    pass



