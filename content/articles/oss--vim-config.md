Title: Built-in Vim Configuration
Category: oss/vim
Tags: oss,vim,writing,linux,code,config
Status: published

My first experience with vim was frustrating, as it is for many. Grown in a world of fully-featured IDEs, vim was barely usable or comprehensible without any configuration.

If I had to learn it again, I would use this configuration as a starting point, and if possible, _without_ plugins. Still maintain a general understanding what each line does. Add plugins incrementally and on a needs basis, so as to understand what the editor itself does, and what _specifically_ plugins do to extend that functionality.

<pre><code class="bash" id="config.vim"></code></pre>
<script>loadFileTextElement("config.vim", "https://raw.githubusercontent.com/rwev/evix/master/.vim/config.vim")</script>


I haven't found much use for custom keybindings, and I picture adding many until [grokking](https://en.wikipedia.org/wiki/Grok#In_computer_programmer_culture) vim, with the exception of plugin integration. My mappings to built-in vim functions are few.

<pre><code class="vim" id="mappings.vim"></code></pre>
<script>loadFileTextElement("mappings.vim", "https://raw.githubusercontent.com/rwev/evix/master/.vim/mappings.vim")</script>


