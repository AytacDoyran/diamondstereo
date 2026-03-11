import os
import yt_dlp
import subprocess


def download_youtube_video(url, output_video):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_video,
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': False,
        'retries': 1,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def extract_audio(input_video, output_wav):
    subprocess.run([
        'ffmpeg', '-y', '-i', input_video, '-vn',
        '-acodec', 'pcm_s16le', '-ac', '2', '-ar', '48000',
        output_wav,
    ], check=True)


def apply_diamond_stereo_effect(input_wav, output_wav):
    subprocess.run([
        'ffmpeg', '-y', '-i', input_wav, '-ac', '2',
        '-filter_complex',
        'channelsplit=channel_layout=stereo[left][right];'
        '[left]adelay=5|0[left_delay];'
        '[right]adelay=0|5[right_delay];'
        '[left_delay][right_delay]amix=inputs=2,volume=2',
        output_wav,
    ], check=True)


def merge_video_audio(video_file, audio_file, output_file):
    subprocess.run([
        'ffmpeg', '-y', '-i', video_file, '-i', audio_file,
        '-ac', '2',
        '-c:v', 'copy', '-c:a', 'aac', '-b:a', '320k',
        '-map', '0:v:0', '-map', '1:a:0',
        output_file,
    ], check=True)


def main():
    try:
        kayit_klasoru = input('💾 Kaydedilecek klasör ismini gir (sadece klasör adı): ').strip()
        if not kayit_klasoru:
            kayit_klasoru = 'DiamondStereoDosyalar'

        if not os.path.exists(kayit_klasoru):
            os.makedirs(kayit_klasoru)

        indirilen_video = os.path.join(kayit_klasoru, 'indirilen_video.mp4')
        gecici_ses = os.path.join(kayit_klasoru, 'gecici_ses.wav')
        duzgun_ses = os.path.join(kayit_klasoru, 'duzgun_ses.wav')
        cikis_video = os.path.join(kayit_klasoru, 'diamond_stereo_video.mp4')

        youtube_url = input('🎥 YouTube video linkini gir: ').strip()

        print('🔵 Video indiriliyor...')
        download_youtube_video(youtube_url, indirilen_video)

        print('🔵 Sesi çıkarıyoruz...')
        extract_audio(indirilen_video, gecici_ses)

        print('🟢 Diamond Stereo efekti uygulanıyor...')
        apply_diamond_stereo_effect(gecici_ses, duzgun_ses)

        print('🟢 Videoya yeni sesi ekliyoruz...')
        merge_video_audio(indirilen_video, duzgun_ses, cikis_video)

        print(f'✅ Bitti! Diamond Stereo dosyan hazır: {cikis_video} 🎶')

    except Exception as e:
        print(f'❌ Hata oluştu: {e}')

    finally:
        input('\nİşlem bitti! Çıkmak için Enter\'a bas...')


if __name__ == '__main__':
    main()
