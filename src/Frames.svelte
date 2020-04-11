<script>
    export let link;
    export let channel;
</script>

<style>
    iframe{
        margin: 10px;
    }
</style>

<widgetbot
  server={link}
  channel={channel}
  width="800"
  height="600"
  shard="https://e.widgetbot.io"
></widgetbot>