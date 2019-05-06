require 'henkei'
require 'epub/parser'
Dir.glob("./files/*") do |filename|
  print filename
  reader = EPUB::Parser.parse(filename)
  newname = filename.sub(/\.[^.]+\z/, '')
  data = Henkei.new "#{filename}"
  file = File.open("#{newname}.txt", "w")
  if (File.extname(filename) == ".epub")
    reader.each_page_on_spine do |page|
      page.media_type = "application/xhtml+xml"
      text = page.content_document.nokogiri
      text.css('style, script').remove
      file.puts text.text
    end
  else
    text = data.text
    puts text
    file.puts text
  end
  file.close
end
