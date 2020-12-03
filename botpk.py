import speech_recognition
from gtts import gTTS
import os
import pyttsx3
import playsound
import webbrowser
from datetime import time
from datetime import date
from datetime import datetime
from youtube_search import YoutubeSearch
#Khởi tạo
bot_brain= "" #Ban đầu chưa học gì nên não chưa có thông tin
# Nghe từ mic
def nghe():
    bot_ear = speech_recognition.Recognizer()#Bot nghe
    with speech_recognition.Microphone() as mic:
        print("\nBot: Tôi đang nghe bạn nói!")
        audio = bot_ear.record(mic, duration= 5) #Bot nghe trong vòng 3 giây sau đó tắt Mic, tránh treo máy do bật Mic lien tục
        print("\nBot: ....")
    try:
        you = bot_ear.recognize_google(audio,language='vi-VN')# Nhờ Google chuyển sang văn bản
        print("\nYou: "+you)
        return you
    except:
        you ="Tôi không hiểu bạn nói gì."
        print("\nBot: "+you)
        noi(you)
    return 0

# Hiểu
def hieux1(text):
    now = datetime.now()
    days = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu', 'Thứ bảy', 'Chủ nhật']
    today = date.today()
    wd = date.weekday(today)
    if "giờ" in text:
        print("\nBot: Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
        noi('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        print("\nBot: Hôm nay là %s, ngày %d tháng %d năm %d" %
              (days[wd], now.day, now.month, now.year))
        noi("Hôm nay là  %s, ngày %d tháng %d năm %d" %
              (days[wd], now.day, now.month, now.year))
    else:
        print("\nBot:Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        noi("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
    return 0
def hieux2(text):
    if "bao nhiêu khu" in text:
        bot_brain ="Xã Tứ Hiệp gồm 14 khu bạn à"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    elif "diện tích" in text:
        bot_brain ="Xã Tứ Hiệp có diện tích 31,959 kilomet vuông"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    elif "dân số" in text:
        bot_brain ="Xã Tứ Hiệp có dân số 7858 người bạn à"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    else:
        print("\nBot:Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        noi("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
    return 0
def hieux3(text):
    if "bao nhiêu xã" in text or "thị trấn" in text:
        bot_brain ="Huyện Hạ Hoà hiện tại gồm 19 xã, 1 thị trấn"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    elif "diện tích" in text:
        bot_brain ="Huyện Hạ Hoà có diện tích tự nhiên 340,147 kilomet vuông"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    elif "dân số" in text or "số dân" in text:
        bot_brain ="Huyện Hạ Hoà có dân số 108889 người bạn à"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    else:
        print("\nBot:Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        noi("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
    return 0
def hieux4(text):
    if "chuyện gì đó" in text or "truyện gì đó" in text:
        bot_brain ="Ngày xửa ngày xưa. Tôi và bạn chưa ai lắm chuyện như vậy. Thôi bạn làm việc đi"
        print("\nBot: "+bot_brain)
        noi(bot_brain)  
    else:
        print("\nBot:Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        noi("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
    return 0
def hieu1(you):
    bot_brain ="Tôi tên là Bot"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu2(you):
    bot_brain ="Tôi vừa mới được sinh ra bởi các bạn học sinh trường Phụ Khánh"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu3(you):
    bot_brain ="Tôi đến từ xã Tứ Hiệp thuộc huyện Hạ Hoà tỉnh Phú Thọ"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu4(you):
    bot_brain ="Tôi thấy rất tuyệt. Không có gì phải than phiền cả"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu5(you):
    bot_brain ="Hãy thôi than vãn đi"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu6(you):
    bot_brain ="Có nhiều bạn à. Đầm Ao Châu, Ao Giời, Suối Tiên, đền Mẫu, đền Chu, đình Nghè..."
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0 
def hieu7(you):
    bot_brain ="Trường tôi rất đẹp và thân thiện. Trường đã đạt chuẩn Quốc gia năm 2016"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0

def hieu8(you):
    bot_brain ="Trường tôi có 26 cán bộ giáo viên"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu9(you):
    bot_brain ="Có 11 lớp bạn à. Trong đó khối 7 có 2 lớp còn các khối khác mỗi khối 3 lớp"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu10(you):
    bot_brain ="Có 387 học sinh. Trong đó khối 6 có 96 bạn khối 7 có 83 bạn, khối 8 có 112 bạn khối 9 có 96 bạn"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu11(you):
    bot_brain ="Là ngôn ngữ dùng để viết chương trình"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu12(you):
    bot_brain ="Gồm bảng chữ cái và các quy tắc"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu13(you):
    bot_brain ="Là những từ dùng với ý nghĩa riêng, không được dùng các từ khóa này cho bất kì mục đích nào khác"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu14(you):
    bot_brain ="Gồm 2 phần. Phần khai báo và phấn thân. Trong đó phần thân bắt buộc phải có"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu15(you):
    bot_brain ="Gồm khai báo tên chương trình, thư viện, hằng, kiểu dữ liệu, chương trình con, biến.."
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu16(you):
    bot_brain ="Phần thân trong Pascal bắt đầu bằng Begin sau đó là dãy các lệnh và kết thúc là End"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu17(you):
    bot_brain ="Gồm 4 cơ bản là kiểu số nguyên, số thực, ký tự và logic"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu18(you):
    bot_brain ="Biến là đại lượng dùng để lưu trữ và giá trị có thể thay đổi khi thực hiện chương trình"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu19(you):
    bot_brain ="Hằng là đại lượng có giá trị không đổi khi thực hiện chương trình"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu20(you):
    bot_brain ="if (điều kiện) then (câu lệnh 1) else (câu lệnh 2);"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu21(you):
    bot_brain ="Lặp với số lần biết trước với for to do và chưa biết trước với While do"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu22(you):
    bot_brain ="Cách khai báo tên biến mảng:array[kiểu chỉ số] of kiểu phần tử;"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu23(you):
    bot_brain ="Cách khai báo (tên biến xâu):string;"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu24(you):
    bot_brain ="Gồm hàm (Function) và thủ tục (Procedure)"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu25(you):
    bot_brain ="Gồm các kiểu cơ bản là byte, integer, word, longint"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu26(you):
    bot_brain ="Được khai báo với tên chuẩn Real"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu27(you):
    bot_brain ="Được khai báo với tên chuẩn Char"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu28(you):
    bot_brain ="Được khai báo với tên chuẩn Real"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu29(you):
    bot_brain ="Function tên hàm(Đối số): kiểu dữ liệu sau đó là phần khai báo và phần thân"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu30(you):
    bot_brain ="Procedure tên thủ tục(Đối số) sau đó là phần khai báo và phần thân"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0
def hieu31(you):
    bot_brain ="Ưu điểm: Là một ngôn ngữ có hình thức sáng sủa, cấu trúc rõ ràng, cú pháp ngắn gọn"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    bot_brain ="Python với tốc độ xử lý nhanh, có thể tạo ra những chương trình từ siêu nhỏ tới cực lớn"
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    bot_brain ="Hạn chế: Không có các thuộc tính như private hay public, không có vòng lặp while và switch."
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    bot_brain ="Mặc dù tốc độ xử lý của Python nhanh hơn PHP nhưng không bằng JAVA và C++."
    print("\nBot: "+bot_brain)
    noi(bot_brain)
    return 0    
# Nói
def noi(you):
    bot_peak = gTTS(text=you, lang='vi', slow=False)
    bot_peak.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")
    return 0
def stop():
    print("\nBot: Hẹn gặp lại bạn sau!")
    noi("Hẹn gặp lại bạn sau!")
# Youtube
def play_nhac(text):
    print('\nBot: Bạn muốn mở bài hát nào?')
    noi("Bạn muốn mở bài hát nào?")
    mysong = nghe()
    url = 'https://www.youtube.com/results?search_query=' + mysong
    webbrowser.open(url)
    print("\nBot: Bài hát bạn yêu cầu đã được mở.")
    noi("Bài hát bạn yêu cầu đã được mở.")
#Tổng hợp
def tonghop():
    noi("Xin chào, bạn cần bot giúp gì ạ?")
    while True:
            you = nghe()
            if you:
                yu=you.upper()
            if not you:
                 break
            elif 'NGÀY NÀO' in yu or 'NGÀY BAO NHIÊU' in yu or 'MẤY GIỜ' in yu or 'THỨ MẤY' in yu:
                hieux1(you)  
            elif 'TỨ HIỆP' in yu:
                hieux2(you) 
            elif 'HẠ HOÀ' in yu or 'HẠ HÒA' in yu:
                hieux3(you)             
            elif 'NGHE CHUYỆN' in yu or 'NGHE TRUYỆN' in yu:
                hieux4(you)        
            elif 'TÊN LÀ GÌ' in yu or 'TÊN GÌ' in yu:
                hieu1(you)
            elif 'BAO NHIÊU TUỔI' in yu or 'MẤY TUỔI' in yu:
                hieu2(you)
            elif 'ĐẾN TỪ ĐÂU' in yu or 'QUÊ Ở ĐÂU' in yu:
                hieu3(you)
            elif 'MUỐN THAN PHIỀN' in yu:
                hieu4(you)
            elif 'MỆT QUÁ' in yu:
                hieu5(you)
            elif 'CÓ THẮNG CẢNH NÀO' in yu:
                hieu6(you)
            elif 'TRƯỜNG CỦA BẠN THẾ NÀO' in yu:
                hieu7(you)                            
            elif 'BAO NHIÊU CÁN BỘ GIÁO VIÊN' in yu:
                hieu8(you)
            elif 'BAO NHIÊU LỚP' in yu:
                hieu9(you)
            elif 'BAO NHIÊU HỌC SINH' in yu:
                hieu10(you)
            elif 'NGÔN NGỮ LẬP TRÌNH LÀ GÌ' in yu:
                hieu11(you)
            elif 'NGÔN NGỮ LẬP TRÌNH GỒM NHỮNG GÌ' in yu:
                hieu12(you)
            elif 'TỪ KHÓA LÀ GÌ' in yu:
                hieu13(you)
            elif 'CẤU TRÚC CHƯƠNG TRÌNH' in yu:
                hieu14(you)
            elif 'PHẦN KHAI BÁO TRONG PASCAL' in yu:
                hieu15(you)
            elif 'PHẦN THÂN CHƯƠNG TRÌNH TRONG PASCAL' in yu:
                hieu16(you)
            elif 'CÁC KIỂU DỮ LIỆU CƠ BẢN TRONG PASCAL' in yu:
                hieu17(you)
            elif 'BIẾN LÀ GÌ' in yu:
                hieu18(you)
            elif 'HẰNG LÀ GÌ' in yu:
                hieu19(you)
            elif 'CẤU TRÚC RẼ NHÁNH TRONG PASCAL' in yu:
                hieu20(you)
            elif 'CẤU TRÚC LẶP TRONG PASCAL' in yu:
                hieu21(you)
            elif 'KIỂU MẢNG TRONG PASCAL' in yu:
                hieu22(you)
            elif 'KIỂU XÂU TRONG PASCAL' in yu:
                hieu23(you)
            elif 'CHƯƠNG TRÌNH CON TRONG PASCAL' in yu:
                hieu24(you)
            elif 'KIỂU SỐ NGUYÊN TRONG PASCAL' in yu:
                hieu25(you)
            elif 'KIỂU SỐ THỰC TRONG PASCAL' in yu:
                hieu26(you)                
            elif 'KIỂU KÝ TỰ TRONG PASCAL' in yu:
                hieu27(you)
            elif 'KIỂU LOGIC TRONG PASCAL' in yu:
                hieu28(you)
            elif 'HÀM TRONG PASCAL' in yu:
                hieu29(you)
            elif 'THỦ TỤC TRONG PASCAL' in yu:
                hieu30(you)
            elif 'ĐẶC ĐIỂM CỦA' in yu:
                hieu31(you)    
            elif 'KHOA HỌC KỸ THUẬT' in yu:
                hieu32(you)
                                                                           
            else:
               noi("Bot chưa nghe rõ. Bạn cần Bot giúp gì ạ?")
    return 0

tonghop()
