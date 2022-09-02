import os


class SubChapterService:
    def __init__(self, chapter, sub_chapter):
        self.chapter = chapter
        self.sub_chapter = None
        self.sub_chapter_path = None
        self.capitalize_first_letters(sub_chapter)
        self.set_sub_chapter_path()

    def capitalize_first_letters(self, sub_chapter):
        if sub_chapter:
            sub_chapter = sub_chapter.split(" ")
            new_sub_chapter = ""
            for word in sub_chapter:
                new_sub_chapter += word[0].capitalize() + word[1:]
            self.sub_chapter = new_sub_chapter + "Animations"

    def set_sub_chapter_path(self):
        if self.chapter:
            chapter_path = os.path.join("videos", self.chapter)
            sub_chapter_path = os.path.join(chapter_path, self.sub_chapter)
            self.sub_chapter_path = sub_chapter_path.replace("\\", "/")

    def get_sub_chapters(self):
        return os.listdir(self.sub_chapter_path)

    def get_sub_chapter_of_sub_chapter_path(self, sub_chapter_of_sub_chapter):
        return os.path.join(self.sub_chapter_path, sub_chapter_of_sub_chapter).replace("\\", "/") + ".mp4"
