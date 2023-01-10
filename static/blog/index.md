---
title: Aleph's lair (WIP)
css: 
- ../../style.css
path: ../../

---

# Welcome!

This is the place where you can find things that I at least find interesting, 
very humbly written by me. I write mainly about two topics: Mathematics and Chess.
I also have a section for "Lies of high school", which is devoted to misconceptions 
that are highly believed to the point that they are assumed to be common knowledge and 
taught in high school.
One classic example of this is: The Earth goes around the Sun and not the other way around. Careful! 
I'm not denying any scientific fact, but stop to think it for a moment. In a world where only the Earth
and the Sun exists, how would you tell which one is rotating around which one? You can't!

Check them out:

<h3>Tags</h3>
<ul id=tagcloud>
<?php
$db = new SQLite3('db/web.sqlite3', SQLITE3_OPEN_READWRITE);

$result = $db->query('select tags from posts where not tags=""');

$tags=array();

while ($row = $result->fetchArray()) {
    $value=$row["tags"];
    if (substr($value,-1)=="/"){
        $value = substr($value,0,-1);
    }

    $curr_tags=explode("/",$value);

    for ($i=0;$i<count($curr_tags);$i++){
        $key=str_replace("_", " ",$curr_tags[$i]);
        $key=ucfirst($key);
        if (in_array($key,array_keys($tags))){ 
            $tags[$key]=1;
        } else {
            $tags[$key]=$tags[$key]+1;
        }
    }
}
foreach (array_keys($tags) as $tag){
    echo "<li>\n";
        echo "\t$tag\n";
    echo "</li>\n";
}
?>
</ul>
