-- Keep long evidence paths and hashes readable without changing their text.
function Code(el)
  if FORMAT:match('latex') and #el.text >= 24
      and el.text:match('^[%w%./_*%-]+$') then
    return pandoc.RawInline('latex', '\\path{' .. el.text .. '}')
  end
end
